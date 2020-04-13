# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:17:28 2020

@author: vk779
"""

n = int(input())
dic =dict()
for z in range(n):
    x= input()
    s= x.split()
    dic1={s[0] : [ s[1],s[2],s[3] ]}
    dic.update(dic1)


y= input()
sum = float(dic[y][0]) + float(dic[y][1]) + float(dic[y][2])
#sum = round((sum/3),2)
print("{:.2f}".format(sum/3))