"""import pandas as pd
"""
from pandas import DataFrame

"""
file = "C:Users\qinweiyi\Desktop\成绩.xlsx"
df = pd.read_excel(file)

print(df)
"""
data = {'姓名':['张飞', '关羽', '刘备', '典韦', '许褚'],'语文': [68, 95, 98, 90, 80],
         '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}

df1 = DataFrame(data, columns=['姓名', '语文', '数学', '英语'])

df2 = df1[['语文', '数学', '英语']].agg(['mean', 'max', 'min', 'var', 'std'])

df1['总成绩'] = df1.sum(axis=1)
df3 = df1.sort_values(by='总成绩', axis=0, ascending=False)

print(df3)
