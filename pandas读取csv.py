# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:39:50 2019

@author: Tuzhirun
"""


import numpy as np
import pandas as pd  
from shapely.geometry import Polygon


df = pd.read_csv('L0003_lingjian.csv')
#num=df.index()
#将数据存储成矩阵形式：
#alt=np.array(df[['下料批次号','零件号','数量','外轮廓','允许旋转角度','面料号']])

alt=np.array(df['外轮廓'])

#多少个零件：314个
num_lingjian=int(len(alt))


##################################将轮廓数据列表化
s=[]
for i in range(num_lingjian):

    if i<num_lingjian:
        s.append(alt[i])    #s中包含314行，每行代表一个零件 type:list
#        print(i)

s_=[]
for m in range(0,num_lingjian):
    s_.append(eval(s[m]))


def cac_Area(num):
    s_1=()
    for n in range(0,num_lingjian):
        s_1=tuple(s_[num])
    return s_1


if  __name__=='__main__':
    area=[]
    for l in range(0,num_lingjian):
        
        s_1=cac_Area(l)
        polygon=Polygon(s_1)
        var_area=polygon.area
        area.append(var_area)

    area_last=np.array(area)
    print("总的零件面积为：{:.12f}".format(np.sum(area_last)))
    