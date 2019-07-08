# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:11:16 2019

@author: zhaoguangjun
"""

def insert_sort(alist):
    '''插入排序'''
    n = len(alist)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
                
def insert_sort1(alist):
    '''插入排序:对于有序序列情况下进行优化'''
    n = len(alist)
    # 从右边的无序序列中取出多少个元素执行这样的过程
    for i in range(1, n):
        # j代表内存循环起始值
        j = i
        # 执行从右边的无序序列中取出第一个元素,即i位置的元素,然后将其
        #插入到前面的正确位置中        
        while j > 0:
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
                j -= 1
            else:
                break

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insert_sort1(li)
    print(li)