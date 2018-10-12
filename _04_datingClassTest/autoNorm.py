#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 11:06
# @Author  : Humeme
# @Site    : 
# @File    : autoNorm.py
# @Software: PyCharm

# 目的：是为了让数据的贡献程度一致

import numpy as np

def autoNorm(dataSet):
	minVals = dataSet.min(0)									# 返回当前列的最小值
	#print('dataSet= ',dataSet)
	maxVals = dataSet.max(0)									# 返回当前列的最大值
	ranges = maxVals - minVals									# 求出当前列的范围
	normDataSet = np.zeros(np.shape(dataSet))					# 返回矩阵 dataSet 的行列数，并创建零矩阵
	m = dataSet.shape[0]										# 得到输入数据的行数
	normDataSet = dataSet - np.tile(minVals, (m,1))				# 计算 oldValue - min
	normDataSet = normDataSet / np.tile(ranges, (m,1))			# 计算 newValue
	return normDataSet,ranges,minVals