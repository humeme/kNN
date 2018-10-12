#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 20:36
# @Author  : Humeme
# @Site    : 
# @File    : appoint.py
# @Software: PyCharm

#将原始数据转为计算机可以分析的numpy数据（输入字符串————>矩阵）

from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import operator
import matplotlib
from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines

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
		#s.split(),将字符串根据 '\t' 分隔符进行切片，然后需要一个列表来装着
		listFromLine = line.split('\t')
		#print(listFromLine[0:3])

		#从第0行到第999行以科学计数法返回		第 0 行的所有列
		returnMat[index,:] = listFromLine[0:3]
		#print(returnMat[index,:])
		classLabel.append(int (listFromLine[-1]))
		index +=1
	return returnMat,classLabel



if __name__ == '__main__':
	#filename = 'datingTestSet2.txt'
	datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')

	fig = plt.figure()														#创建画布
	ax1 = fig.add_subplot(311)												#对画布进行分区
	#plt.xlabel('w')
	ax1.scatter(datingDataMat[:,1], datingDataMat[:,2])						#在画布 1 区作点图

	ax2 = fig.add_subplot(312)
	#plt.xlabel('the time of play game')									# 给 X 轴创建标签
	ax2.scatter(datingDataMat[:, 1], datingDataMat[:, 2],
				15.0 * array(datingLabels), 15.0 * array(datingLabels))		#在画布 2 区作点图

	ax3 = fig.add_subplot(313)
	ax3.scatter(datingDataMat[:,0],datingDataMat[:,1],
				 15.0 * array(datingLabels), 15.0 * array(datingLabels))
	#ax3.plot(datingDataMat[:,0],datingDataMat[:,1],						这里是作线图
			# 15.0 * array(datingLabels), 15.0 * array(datingLabels))

	plt.show()
	# plt.savefig('demo.pdf')		无用

	print ('datingDataMat= \n',datingDataMat)
	print ('datingLabels= \n', datingLabels[0:20])