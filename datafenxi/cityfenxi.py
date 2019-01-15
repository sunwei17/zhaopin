# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use('qt4agg')
from pylab import mpl
from matplotlib.font_manager import *

from webtest.models import listtwo

xitongjicheng = listtwo.objects.filter()[0:4]

myfont = FontProperties(fname='/System/Library/Fonts/STHeiti Medium.ttc')

mpl.rcParams['axes.unicode_minus'] = False

'''
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
df = pd.DataFrame(data, index=df['Name'])



df = df.dropna()
plt.figure()
df.plot(kind = 'bar', title='test')
plt.savefig('img.png')
print (df)
'''

"""
plt.figure()
plt.pie([1, 1, 3, 5], labels=['one', 'two', 'three', 'four'])
plt.savefig('t.png')
"""
file = pd.read_excel('/Users/sunwei/Documents/商品.xlsx', encoding="gb2312")
#print(file['商品名'])
list = []
list2 = []
for i in range(0, len(file['商品名'])):
    list.append(file['商品名'][i].encode("utf-8").decode("utf-8"))
    list2.append(file['价格'][i])
plt.pie(file['价格'], labels=list)
#plt.savefig('t.png')


plt.figure()
data = {
    "name": list,
    "price": list2
}
df = pd.DataFrame(data, index=data['name'])
df.plot(kind = 'bar', title='测试')
#plt.savefig('img.png')
plt.show()
#print (matplotlib.matplotlib_fname())
