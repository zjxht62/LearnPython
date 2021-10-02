import requests
import json
import time
import schedule
import matplotlib.pyplot as plt
import matplotlib

from database import DbHelper

params = {'page': 1, 'page_size': 1000}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
db_helper = DbHelper()
db_helper.get_db_connection(host="192.168.50.53", user_name='root',
                            password='c9r6e2h7', db='zjx')
db_helper.exec_select_sql("select * from t_universal_waiting")


def get_data():
    print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    r = requests.get(
        "https://gw.app.universalbeijingresort.com/attraction/list",
        params=params,
        headers=headers)

    json_result = r.text
    result_dict = json.loads(json_result)
    rides_list = result_dict['data']['list']
    for ride in rides_list:
        db_helper.get_db_connection(host="192.168.50.53", user_name='root',
                                    password='12345678', db='aaa')
        print(f"项目：{ride['title']}，的等待时间是：{ride['waiting_time']}")
        sql = "INSERT INTO `zjx`.`t_universal_waiting`(`ride_id`, `ride_title`, `waiting_time`, `gems_status`, `insert_time`) VALUES ('{}', '{}', '{}', '{}', '{}');"
        db_helper.exec_update(
            sql.format(ride['id'], ride['title'], ride['waiting_time'],
                       ride['gems_status'], current_time))

def collect_data():
    schedule.every(10).minutes.do(get_data)
    while True:
        schedule.run_pending()
        time.sleep(1)

def generate_line_chart(ride_id):
    db_helper.get_db_connection(host="192.168.50.53", user_name='root',
                                password='c9r6e2h7', db='zjx')
    data = db_helper.exec_select_sql("select * from t_universal_waiting where ride_id = '{}' AND insert_time BETWEEN '2021-09-22 08:00:00' and '2021-09-22 21:00:00'".format(ride_id))
    waiting_time_list = [i[3] for i in data]
    collect_time_list = [j[5] for j in data]

    #
    # dates = matplotlib.dates.date2num(list_of_datetimes)
    # matplotlib.pyplot.plot_date(dates, values)

    print(waiting_time_list)
    print(collect_time_list)
    plt.plot(collect_time_list,waiting_time_list)
    plt.gcf().autofmt_xdate()

    plt.show()



if __name__ == '__main__':
    generate_line_chart("5fa22624dcb5e53c6c72ab42")


