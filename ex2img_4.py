#!/usr/bin/python3
#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from xlrd import open_workbook
from pylab import *

x_data=[]
y_data=[]
x_data1=[]
y_data1=[]
x_data2=[]
y_data2=[]
x_data3=[]
y_data3=[]
x_volte=[]
temp=[]


plt.annotate('Close loop point',size=18, xy=(180, 0.1), xycoords='data',
                xytext=(-100, 40), textcoords='offset points',
                arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2")
                )
# plt.annotate(' ', xy=(0, -0.1), xycoords='data',
#                 xytext=(200, -90), textcoords='offset points',
#                 arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=-.2")
#                 )
plt.annotate('Zero point in non-monotonic region', size=18,xy=(360, 0), xycoords='data',
                xytext=(-290, -110), textcoords='offset points',
                arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2")
                )

# wb = open_workbook('phase_detector.xlsx')
# for s in wb.sheets():
#     print('Sheet:',s.name)
#     for row in range(s.nrows):
#         print('the row is:',row)
#         values = []
#         for col in range(s.ncols):
#             values.append(s.cell(row,col).value)
#         print(values)
#         x_data1.append(values[0])
#         y_data1.append(values[1])
# plt.plot(x_data1, y_data1, 'g',label=u"Original",linewidth=2)

# wb = open_workbook('phase_detector2.xlsx')
# for s in wb.sheets():
#     print('Sheet:',s.name)
#     for row in range(s.nrows):
#         print('the row is:',row)
#         values = []
#         for col in range(s.ncols):
#             values.append(s.cell(row,col).value)
#         print(values)
#         x_data2.append(values[0])
#         y_data2.append(values[1])
# plt.plot(x_data2, y_data2, 'r',label=u"Move the pullup resistor",linewidth=2)



# wb = open_workbook('my_data.xlsx')
# for s in wb.sheets():
#     print('Sheet:',s.name)
#     for row in range(s.nrows):
#         print('the row is:',row)
#         values = []
#         for col in range(s.ncols):
#             values.append(s.cell(row,col).value)
#         print(values)
#         x_data.append(values[0])
#         y_data.append(values[1])
# plt.plot(x_data, y_data, 'b',label=u"Faster D latch and XOR",linewidth=2)

for i in range(360):
    x_data3.append(i)
    y_data3.append((i-180)*0.052-0.092)
plt.plot(x_data3, y_data3, 'b--',label=u"The Ideal Curve",linewidth=2)

#plt.title(u"2 \pi phase detector", fontproperties=font)
plt.title(u"$2\pi$ phase detector",size=20)
plt.legend(loc=0)#显示label
#移动坐标轴代码
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))



plt.xlabel(u"$\phi/deg$",size=20)
plt.ylabel(u"$DC/V$",size=20)

plt.show()
print('over!')