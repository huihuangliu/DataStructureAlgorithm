# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:27:09 2019

@author: zhaoguangjun
"""

def bubble_sort(alist):
    '''冒泡排序'''
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]: 
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
            if count == 0:  # 优化
                break

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)
    