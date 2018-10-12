#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 13:33
# @Author  : Humeme
# @Site    : 湘潭大学
# @File    : img2vector.py
# @Software: PyCharm

import numpy as np

def img2vector (filename):									# 创建一个 1*1024 的向量
	returnVect = np.zeros((1,1024))
	fr = open(filename)										# 读取文件
	for i in range(32):										# 循环处理 32 行
		lineStr = fr.readline()								# 读取每一行
		for j in range(32):									# 循环处理 32 列
			returnVect[0, 32 * i + j] = int(lineStr[j])		# 把每一行的数据读到 1*1024 的向量中去,这里是一个一个的读进去的。
	return returnVect