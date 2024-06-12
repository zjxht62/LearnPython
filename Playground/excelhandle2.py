import pandas as pd

# 读取 Excel 文件 A 和 B
df_a = pd.read_excel('2023年12月1起至今（销售出库）-已合并.xlsx')
df_b = pd.read_excel('成品历史维修记录2024年5月28日-第二版.xlsx')

# 获取 A 表和 B 表的第 12 列和第 8 列数据
a_twelfth_column = df_a.iloc[:, 11]
b_eighth_column = df_b.iloc[:, 7]

# 将 B 表中第 8 列数据作为字典，方便查询
b_eighth_dict = dict(zip(b_eighth_column, df_b.index))

# 遍历 A 表中的每一行
for index, row in df_a.iterrows():
    # 获取 A 表当前行的第 12 列数据
    a_value = row.iloc[11]

    # 如果当前行的第 12 列数据在 B 表的第 8 列中存在
    if a_value in b_eighth_dict:
        # 获取 B 表中对应行的索引
        b_index = b_eighth_dict[a_value]

        # 获取 B 表中对应行的第 9 列和第 10 列数据
        b_ninth_value = df_b.iloc[b_index, 8]
        b_tenth_value = df_b.iloc[b_index, 9]
        b_11th_value = df_b.iloc[b_index, 10]

        print(a_value)
        print('第9列',b_ninth_value)
        print('第10列',b_tenth_value)
        print('第11列',b_11th_value)

        # # 将 B 表中对应行的第 9 列和第 10 列数据追加到 A 表中对应行的后面
        df_a.at[index, 'N'] = b_ninth_value
        df_a.at[index, 'O'] = b_tenth_value
        df_a.at[index, 'p'] = b_11th_value

# 将处理后的 A 表保存到新的 Excel 文件中
df_a.to_excel('output_excel_file.xlsx', index=False)
