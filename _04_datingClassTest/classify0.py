#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 11:09
# @Author  : Humeme
# @Site    : 
# @File    : classify0.py
# @Software: PyCharm

import numpy as np
import operator

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]					#返回训练集的行数
	diffMat = np.tile (inX, (dataSetSize,1)) - dataSet	#利用tile函数求出差
	sqDiffMat = diffMat ** 2						#对差求平方
	sqDistances = sqDiffMat.sum(axis = 1)			#对平方求和，axis=1按行相加
	distances = sqDistances ** 0.5					#开根号得欧式距离
	sortedDistances = distances.argsort()		#对距离按从小到大的次序排列，(2,3,0,1)
	classCount = {}									#（'B':2, 'A':1)
	for i in range(k):
			voteIlabel = labels[sortedDistances[i]]
			classCount [voteIlabel] = classCount.get(voteIlabel, 0) + 1
	#print(classCount.items())						dict_items([('A', 1), ('B', 2)])

	#首先以列表返回可遍历的数组，然后以第二项为标准进行比较，用逆序的形式。 sorted（）提供允许对可迭代对象进行排序功能。
	sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
	#print(sortedClassCount)
	#print (sortedClassCount[1] [0])
	#print (sortedClassCount)
	return sortedClassCount[0] [0]