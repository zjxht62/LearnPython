months = [
    'January',
    "February",
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

endings = ['st', 'nd', 'rd'] \
          + 17 * ['th'] \
          + ['st', 'nd', 'rd'] \
          + 7 * ['th'] \
          + ['st']

#input获取到的是字符串类型
year = input("请输入年份")
month = input('请输入月份')
day = input('请输入日期')

#字符串转int
monthNumber = int(month)
dayNumber = int(day)

monthString = months[monthNumber - 1]
#字符串拼接
dayString = day + endings[dayNumber - 1]

print(monthString + ' ' + dayString + ', ' + year)


