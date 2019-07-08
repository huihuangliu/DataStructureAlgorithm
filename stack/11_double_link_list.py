# -*- coding: utf-8 -*-
"""
Created on Sat May 18 19:11:05 2019

@author: zhaoguangjun
"""

class Node(object):
    '''节点'''
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None
        

    
class DoubleLinkList(object):
    '''双链表'''
    def __init__(self, node=None):
        self.__head = node 
    
    def is_empty(self):
        '''链表是否为空'''
        return self.__head is None
        
    def length(self):
        '''链表长度'''
        # cur游标,用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while (cur != None):
            count += 1
            cur = cur.next
        return count
    
    def travel(self):
        '''遍历整个链表'''
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print('')
        
    def add(self, item):
        '''链表头部插入节点, 头插法'''
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node
    
    def append(self, item):
        '''链表尾部插入节点, 尾插法'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur
        
    
    def insert(self, pos, item):
        '''指定位置添加元素
        :param pos 从0开始
        '''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            # 当循环退出后cur指向pos的位置
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
    
    def remove(self, item):
        '''删除节点'''
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                # 头节点
                if cur == self.__head:
                   self.__head = cur.next 
                   if cur.next:
                       # 判断链表是否只有一个节点
                       cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next
     
    def search(self, item):
        '''查找节点是否存在'''
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    dll = DoubleLinkList()
    print(dll.is_empty)
    print(dll.length())
    
    dll.append(1)
    print(dll.is_empty)
    print(dll.length())
     
    dll.append(2)
    dll.add(8)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    # 8 1 2 3 4 5 6 
    dll.insert(-1, 9) # 9 8 1 2 3 4 5 6
    dll.travel()
    dll.insert(3, 100)  # 9 8 1 100 2 3 4 5 6
    dll.travel()
    dll.insert(10, 200) # 9 8 1 100 2 3 4 5 6 200
    dll.travel()
    dll.remove(100)
    dll.travel()
    dll.remove(9)
    dll.travel()
    dll.remove(200)
    dll.travel()
    
    
    
    
    
    