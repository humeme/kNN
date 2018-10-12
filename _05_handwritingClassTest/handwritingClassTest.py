#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 12:50
# @Author  : Humeme
# @Site    : 湘潭大学
# @File    : handwritingClassTest.py
# @Software: PyCharm

from os import listdir
from img2vector import img2vector
from classify0 import classify0
import numpy as np
import datetime

def handwritingClassTest():
	traininFilelist = listdir('trainingDigits')							# 读取训练文件夹。
	m = len (traininFilelist)											# 计算文件夹个数，为循环处理提供循环次数
	trainMat = np.zeros((m, 1024))										# 初始化训练包
	labelMat = []														# 创建标签包
	for i in range (m):													# 循环处理训练文件夹
		fileNameStr = traininFilelist[i]								# 读取测试文件的文件名
		fileStr = fileNameStr.split('.')[0]								# 将 '.' 之前的文件名读出来
		fileNumStr = int (fileStr.split('_')[0])						# 将 '_' 之前的数字读出来
		labelMat.append (fileNumStr)									# 将数字添加到标签包中去
		trainMat[i,:] = img2vector('trainingDigits/%s' %fileNameStr)			# 处理单个文件中的数据并赋给训练包
	testFileStr = listdir ('testDigits')								# 读取测试文件夹
	n = len (testFileStr)												# 计算测试文件夹个数，为循环处理提供循环次数
	errorCount = 0.0													# 初始化错误的个数
	for i in range (n):													# 循环处理测试文件夹
		fileNameStr = testFileStr[i]									# 读取训练文件的文件名
		fileStr = fileNameStr.split ('.')[0]							# 将 '.' 之前的文件名读出来
		fileNumStr = int (fileStr.split ('_')[0])						# 将 '_' 之前的数字读出来
		testMat = img2vector ('testDigits/%s' % fileNameStr)			# 处理单个文件中的数据并赋给测试包，注意这里的数据是一行
		classifyResult = classify0 (testMat, trainMat, labelMat, 3)		# 开始进行分类
		print ('反馈是：%s，原来是：%s' % (classifyResult,fileNumStr))	# 显示出来
		if (classifyResult != fileNumStr):								# 判断分类结果是否正确
			errorCount += 1.0
	print ('总共错了 %d 个' % errorCount)
	print ('错误率为：%f' % (errorCount / float(n)))
	print('正确率为：%f' % (1.0 - (errorCount / float(n))))

if __name__ == '__main__':
	starttime = datetime.datetime.now()

	handwritingClassTest()

	endtime = datetime.datetime.now()

	print ('endtime - starttime= ', endtime - starttime)

