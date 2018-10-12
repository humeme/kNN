#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 11:02
# @Author  : Humeme
# @Site    : 
# @File    : autoNorm.py
# @Software: PyCharm

import appoint
import numpy as np

# newValue = (oldValue - min) / (max - min)

def autoNorm(dataSet):
	minVals = dataSet.min(0)									# 返回当前列的最小值，总共有三列
	#print('dataSet= ',dataSet)
	maxVals = dataSet.max(0)									# 返回当前列的最大值，总共有三列
	ranges = maxVals - minVals									# 求出当前列的范围，总共有三列
	normDataSet = np.zeros(np.shape(dataSet))					# 返回矩阵 dataSet 的行列数，并创建零矩阵
	m = dataSet.shape[0]										# 得到输入数据的行数
	normDataSet = dataSet - np.tile(minVals, (m,1))				# 计算 oldValue - min
	normDataSet = normDataSet / np.tile(ranges, (m,1))			# 计算 newValue
	return normDataSet,ranges,minVals



if __name__ == '__main__':
	fr = 'datingTestSet2.txt'
	appoint.file2matrix(fr)
	datingDataMat, datingDataLabel = appoint.file2matrix(fr)

	normMat,ranges,minVals = autoNorm(datingDataMat)
	print ('normMat= \n',normMat)							#归一化
	print ('\nranges= \n',ranges)							#范围
	print ('\nminVals= \n',minVals)							#最小值

	#print ('datingDataMat= \n' ,datingDataMat)
	#print ('datingDataLabel= \n' , datingDataLabel[0:20])