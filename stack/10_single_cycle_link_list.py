# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:50:02 2019

@author: zhaoguangjun
"""


class Node(object):
    '''节点'''
    def __init__(self, item):
        self.elem = item
        self.next = None
    
class SingleCycleLinkList(object):
    '''单向循环链表'''
    def __init__(self, node=None):
        self.__head = node 
        #如果不是空链表
        if node:
            node.next = node
    
    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None
        
    def length(self):
        '''链表长度'''
        # cur游标,用来移动遍历节点
        if self.is_empty():
            return 0
        cur = self.__head
        # count记录数量
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count
    
    def travel(self):
        '''遍历整个链表'''
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        # 退出循环,cur指向尾节点,但是尾节点没打印
        print(cur.elem, end=' ')
        print('')
        
    def add(self, item):
        '''链表头部插入节点, 头插法'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环,cur指向尾节点
            node.next = self.__head
            self.__head = node
            cur.next = node    
    
    def append(self, item):
        '''链表尾部插入节点, 尾插法'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
        
    
    def insert(self, pos, item):
        '''指定位置添加元素
        :param pos 从0开始
        '''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 当循环退出后pre指向pos-1的位置
            node = Node(item)
            node.next = pre.next
            pre.next = node
    
    def remove(self, item):
        '''删除节点'''
        if self.is_empty():
            return False
        pre = None
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                if cur == self.__head:
                    # 头节点的情况
                    # 找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next                
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环,cur指向尾节点
        if cur.elem == item:
            if cur == self.__head:
                # 链表只有一个节点
                self.__head = None
            else:
                pre.next = cur.next
     
    def search(self, item):
        '''查找节点是否存在'''
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环,cur指向尾节点
        if cur.elem == item:
            return True
        return False


if __name__ == '__main__':
    ll = SingleCycleLinkList()
    print(ll.is_empty)
    print(ll.length())
    
    ll.append(1)
    print(ll.is_empty)
    print(ll.length())
    
    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6 
    ll.insert(-1, 9) # 9 8 1 2 3 4 5 6
    ll.travel()
    ll.insert(3, 100)  # 9 8 1 100 2 3 4 5 6
    ll.travel()
    ll.insert(10, 200) # 9 8 1 100 2 3 4 5 6 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
