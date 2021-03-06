#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 11:05
# @Author  : Humeme
# @Site    : 
# @File    : file2matrix.py
# @Software: PyCharm

import numpy as np

def file2matrix(filename):
	fr = open (filename)
	arrayOfLines = fr.readlines()
	numberOfLines = len (arrayOfLines)
	#print ('numberOfLines= ',numberOfLines)
	returnMat = np.zeros ((numberOfLines,3))
	#建立一个空列表
	classLabel = []
	index = 0
	for line in arrayOfLines:
		#s.strip(rm),当rm为空时，默认删除空白字符（'\n','\r','\t',' '）
		line = line.strip()
		#s.split(),将字符串根据 '\t' 分隔符进行切片
		listFromLine = line.split('\t')
		#print(listFromLine[0:3])

		#从第0行到第999行以科学计数法返回		第 0 行的所有列
		returnMat[index,:] = listFromLine[0:3]
		#print(returnMat[index,:])
		classLabel.append(int (listFromLine[-1]))
		index +=1
	return returnMat,classLabel