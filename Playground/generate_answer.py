import xlrd

temp_str = '''
vars.put("answer1","{}");
vars.put("answer2","{}");
vars.put("answer3_weight","{}");
vars.put("answer3_height","{}");
vars.put("answer3_bmi","{}");
vars.put("answer4","{}");
vars.put("answer5","{}");
vars.put("answer6","A03");
vars.put("answer6_1","A01");
vars.put("answer7","A02");
vars.put("answer8","A03");
vars.put("answer9","{}");
vars.put("answer10","A05");
vars.put("answer11","{}");
'''

data = xlrd.open_workbook("测试数据.xls")
table = data.sheets()[0]
for i in range(1, 26):
    print(f'Case-{i}')
    row_value_list = table.row_values(i)
    a1 = row_value_list[0]
    a2 = row_value_list[1]
    a3_w = int(row_value_list[2])
    a3_h = int(row_value_list[3])
    a3_bmi = row_value_list[4]
    a4 = row_value_list[5]
    a5 = row_value_list[6]
    a9 = row_value_list[7]
    a11 = row_value_list[8]
    print(temp_str.format(a1, a2, a3_w, a3_h, a3_bmi, a4, a5, a9, a11))