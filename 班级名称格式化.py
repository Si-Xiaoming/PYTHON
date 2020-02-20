import re
import pandas as pd
import numpy as np
import openpyxl
d=pd.read_excel('129.xlsx')
list=[]
S2h={'0':'零','1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九',
     '九':'9','八':'8','七':'7','六':'6','五':'5','四':'4','三':'3','二':'2','一':'1','零':'0'}
for i in d['1、支部名称']:
    if i[0] in['测','环','地','遥','消','资']:
        result = re.compile(r'(["环""测""遥""地""资""消""测"]["境""绘""感""信""质""勘""防""工"]).*(1[6789]).*([一二三四五六七八九茅1-9])')
        results = result.findall(i)
        add = '20{0}级{1}第{2}团支部'.format(results[0][1], results[0][0], results[0][2])
        print(add)
        list.append(add)
    else:
        result = re.compile(r'.*(1[6789]).*(["环""测""遥""地""资""消""测"]["境""绘""感""信""质""勘""防""工"]).*([一二三四五六七八九茅1-9])')
        results=result.findall(i)
        add='20{0}级{1}第{2}团支部'.format(results[0][0],results[0][1],results[0][2])
        list.append(add)
for it,index in enumerate(list):
    oldstr=str(index)
    if oldstr.find("茅")!=-1:

        newstr=oldstr[:5]+"测绘茅以升团支部"
        list[it]=newstr
        print(newstr)
    elif re.compile(r'\d').findall(oldstr[4:])!=[]:
        app=S2h[oldstr[-4]]
        newstr=oldstr[:-4]+app+oldstr[-3:]
        list[it]=newstr
    else:
        pass
print(list)
p=pd.Series(list)
p.to_excel('asd.xlsx')
