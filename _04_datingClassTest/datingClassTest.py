#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 10:41
# @Author  : Humeme
# @Site    : 
# @File    : datingClassTest.py
# @Software: PyCharm

import operator
#from autoNorm import autoNorm
#from file2matrix import file2matrix
#from classify0 import classify0
import autoNorm
import file2matrix
import classify0
import numpy as np



def datingClassTest():
	datingDataMat, datingLabels = file2matrix.file2matrix('datingTestSet2.txt')		# 读取文本数据
	normMat, ranges, minVals = autoNorm.autoNorm(datingDataMat)						# 对数据归一化处理
	hoRatio = 0.15															# 测试数据的比例
	m = normMat.shape[0]													# 总共数据的数目 1000
	numTest = int (m * hoRatio)												# 测试的数据     100
	errorCount = 0.0															# 判断错误数的初始化
	for i in range(numTest):												# 循环判断测试数据
		# 得到测试结果
		classifyResult = classify0.classify0(normMat[i,:], normMat[numTest:m,:],
								   datingLabels[numTest:m], 3)
		print ('测试结果是：%d，原始结果是：%d' % (classifyResult,datingLabels[i]))
		# 得到错误的个数，来方便计算错误率
		if(classifyResult != datingLabels[i]):
			errorCount += 1.0
	print ('错误率是：%f' % (errorCount / float(numTest)))
	print ('总共错了：%d 个' % (errorCount))

if __name__ == '__main__':
	datingClassTest()