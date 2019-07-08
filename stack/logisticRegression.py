# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:16:57 2019

@author: zhaoguangjun
"""

import numpy as np
import matplot.pyplot as plt
import pandas as pd
import numpy.random
import time

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def model(x, theta):
    return sigmoid(np.dot(x, theta.T))

def cost(X, y, theta):
    left = np.multiply(-y, np.log(model(X, theta)))
    right = np.multiply(1 - y, np.log(1 - model(X, theta)))
    return np.sum(left - right) / len(X)

def gradient(X, y, theta):
    grad = np.zeros(theta.shape)
    error = (model(X, theta) - y).ravel()
    for j in range(len(theta.ravel())):  # for each parameter
        term = np.multiply(error, X[:, j])
        grad[0, j] = np.sum(term) / len(X)
    
    return grad

STOP_ITER = 0
STOP_COST = 1
STOP_GRAD = 2

def stopCriterion(Type, value, threshold):
    #设定三种不同的停止策略
    if Type == STOP_ITER:    return value > threshold
    elif Type == STOP_COST:  return abs(value[-1]-value[-2]) < threshold
    elif Type == STOP_GRAD:  return np.linalg.norm(value) < threshold

def shuffleData(data):
    np.random.shuffle(data)
    cols = data.shape[1]
    X = data[:, 0:cols-1]
    y = data[:, cols-1:]
    return X, y

def descent(data, theta, n, batchSize, stopType, thresh, alpha):
    # 梯度下降
    init_time = time.time()
    i = 0
    k = 0
    X, y = shuffleData(data)
    grad = np.zeros(theta.shape)   #计算的梯度
    costs = [cost(X, y, theta)] #损失值

    while True:
        grad = gradient(X[k:k+batchSize], y[k:k+batchSize], theta)
        k += batchSize    #取batch数量个数据
        if k >= n:
            k = 0
            X, y = shuffleData(data)
        theta = theta - alpha*grad    #参数更新
        costs.append(cost(X, y, theta))   #计算新的损失
        i += 1
        
        if stopType == STOP_ITER:       value = i
        elif stopType == STOP_COST:     value = costs
        elif stopType == STOP_GRAD:     value = grad
        if stopCriterion(stopType, value, thresh): break
    
    return theta, i-1, costs, time.time()-init_time
        