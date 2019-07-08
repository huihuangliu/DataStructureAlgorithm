# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:51:04 2019

@author: zhaoguangjun
"""

def select_sort(alist):
    '''选择排序'''
    new_alist = []
    while len(alist) > 1:
        min_value = min(alist)
        new_alist.append(min_value)
        alist.remove(min_value)
    new_alist.append(alist[0])
    return new_alist

def select_sort1(alist):
    '''选择排序'''
    n = len(alist)
    for j in range(0, n-1):
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]
        
    
li = [54, 26, 54, 93, 17, 77, 31, 44, 55, 20]
print(li)
new_alist = select_sort(li.copy())
print('my work: ', new_alist)        

select_sort1(li)
print('standard: ', li)
        
        
        
        