# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:39:43 2019

@author: zhaoguangjun
"""

def merge_sort(alist):
    '''归并排序'''
    n = len(alist)
    if n <= 1:
        return alist
    # 拆分数组
    mid = n//2
    # left采用归并排序后形成的有序的新的列表
    left_li = merge_sort(alist[:mid])
    
    # right采用归并排序后形成的有序的新的列表
    right_li = merge_sort(alist[mid:])
    
    # 将两个有序的子序列合并为一个新的整体
    left_pointer, right_pointer = 0, 0
    result = []
    
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else: 
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    sorted_list = merge_sort(li)
    print(sorted_list)        
    