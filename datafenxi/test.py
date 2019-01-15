# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use('qt4agg')
from pylab import mpl
from matplotlib.font_manager import *
from webtest.models import citycount
from mongoengine import connect
myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf')
mpl.rcParams['axes.unicode_minus'] = False

connect('zhaopin')
xitongjicheng = citycount.objects.filter()
list1 = []
list2 = []
for item in xitongjicheng:
    list1.append(item.cityname)
    list2.append(int(item.shuliang))

#plt.figure()
data = {
    "name": list1,
    "price": list2
}
print (data)
df = pd.DataFrame(data, index=data['name'])
ax = df.plot(kind = 'bar',title=u'招聘')
for label in ax.get_xticklabels() :
    label.set_fontproperties(myfont)
plt.savefig('te.png')
# df.plot(kind = 'bar', title='test')
# plt.show()