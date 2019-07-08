# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:43:26 2019

@author: zhaoguangjun
"""

import math
from collections import deque

def print_tree(array): #打印堆排序使用
    '''
    深度 前空格 元素间空格
    1     7       0
    2     3       7
    3     1       3
    4     0       1
    '''
    # first=[0]
    # first.extend(array)
    # array=first
    index = 1
    depth = math.ceil(math.log2(len(array))) # 因为补0了，不然应该是math.ceil(math.log2(len(array)+1))
    sep = '  '
    for i in range(depth):
        offset = 2 ** i
        print(sep * (2 ** (depth - i - 1) - 1), end='')
        line = array[index:index + offset]
        for j, x in enumerate(line):
            print("{:>{}}".format(x, len(sep)), end='')
            interval = 0 if i == 0 else 2 ** (depth - i) - 1
            if j < len(line) - 1:
                print(sep * interval, end='')
        index += offset
        print()

def swap_param(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L

def heap_adjust(L, start, end):
    # 调整大顶堆
    temp = L[start]
    
    i = start
    j = 2 * i  # 左孩子节点索引2*i, 右孩子节点索引为2*i+1
    
    while j <= end:
        if (j < end) and (L[j] < L[j+1]): # 左右孩子节点比较
            j += 1       
        if temp < L[j]:  # 先比较右孩子节点,选出大的和父节点比较
            L[i] = L[j]  # 和父节点交换
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp
    
def heap_sort(L):
    '''
    堆排序,采用大根堆 升序
    '''
    L_length = len(L) - 1
    
    # 得到初始最大根堆
    first_sort_count = L_length // 2  # 最后一个非叶子节点
    for i in range(first_sort_count): # 遍历每个非叶子节点
        heap_adjust(L, first_sort_count - i, L_length)
        #print(L)
        
    for i in range(L_length - 1):  # 大根堆最大值和最右下节点交换
        L = swap_param(L, 1, L_length - i)
        heap_adjust(L, 1, L_length - i - 1) # 重新构造大根堆
    
    return [L[i] for i in range(1, len(L))]
    
    
if __name__ == '__main__':
    
    #alist = [0, 6, 8, 2, 3, 9, 7, 4, 1, 5, 10]
    alist = deque([16, 7, 3, 20, 17, 8])
    alist.appendleft(0)
    print(heap_sort(alist))
    
    
    
    
    