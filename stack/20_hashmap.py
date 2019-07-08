# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:34:41 2019

@author: zhaoguangjun
"""

#使用List实现一个哈希表

class Hashmap:
    def __init__(self, mapSize):
        self.mapSize = mapSize    # table size
        self.map = [None] * self.mapSize  # init hash table
    
    def _get_hash_(self, key):
        '''
        哈希函数
        index = sum(ASCII value for each letter in key)%mapSize
        '''
        hash_value = 0
        for char in key:
            hash_value += ord(char)
            
        return hash_value % self.mapSize
    
    def add(self, key, value):
        '''
        添加元素
        '''
        key_hash = self._get_hash_(key)   # 先拿到此key的哈希值
        key_value = [key, value]   # key-value对要一起放在list里面
        
        if self.map[key_hash] is None:
            # key_value再嵌套一个list
            self.map[key_hash] = list([key_value])
            return True
        else:
            # 如果已经存在,遍历,如果找到了,则修改对应的值
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            
            #如果没有找到,则添加到后面
            self.map[key_hash].append(key_value)
            return True
        
    def get(self, key):
        '''
        获取元素
        '''
        hash_value = self._get_hash_(key)
        if self.map[hash_value] is not None:
            for pair in self.map[hash_value]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        '''
        删除元素
        '''
        hash_value = self._get_hash_(key)
        if self.map[hash_value] is not None:
            for i in range(len(self.map[hash_value])):
                if self.map[hash_value][i][0] == key:
                    self.map[hash_value].pop(i)
                    return True
        return False
        
        
        
hashtabel = Hashmap(6)                   
hashtabel.add('Corn', 2.38) 
hashtabel.add('Beans', 1.85)
hashtabel.add('Rice', 1.92)               
print(hashtabel.get('Rice'))                
hashtabel.delete('Rice')  
print(hashtabel.get('Rice'))                
                   
        
        
        
        
        
        