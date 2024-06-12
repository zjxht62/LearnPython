import pandas as pd
import re

# 读取 Excel 文件
df = pd.read_excel('2023年12月1起至今（销售出库）.xlsx')

# 创建一个空的 DataFrame 用于存放拆分后的数据
new_rows = []

# 遍历每一行数据
for index, row in df.iterrows():
    # 获取当前单元格的数据
    data = re.split('/|、|，', row[11])  # 使用正则表达式同时处理 / 和 、 分隔符

    # 如果数据中有多个元素，则拆分成多行数据
    if len(data) > 1:
        for d in data:
            # 创建一个新行数据，复制当前行的其他列数据
            new_row = row.copy()
            new_row[11] = d.strip()  # 去除空白字符
            new_rows.append(new_row)
    else:
        # 如果数据只有一个元素，则直接添加到新行数据中
        new_rows.append(row)

# 将新行数据组合成 DataFrame
new_df = pd.DataFrame(new_rows)

# 将拆分后的数据保存到新的 Excel 文件中
new_df.to_excel('output_excel_file.xlsx', index=False)
