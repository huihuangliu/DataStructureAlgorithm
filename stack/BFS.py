# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:47:30 2019

@author: zhaoguangjun
"""

graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['C', 'D'],
        'F': ['D']
        }

def BFS(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    parent = {s: None}
    while (len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        print(vertex, end=' ')
    return parent

def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while (len(stack) > 0):
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex, end=' ')


parent = BFS(graph, 'E')
print(' ')
for key in parent:
    print(key, parent[key])
print(' ')

# 求最短路径,其中两个节点之间为单位长度
v = 'B'   
while v != None:
    print(v, end=' ')
    v = parent[v]
    
print(' ')
DFS(graph, 'E')



