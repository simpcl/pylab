#!/usr/bin/python3

from linklist import *

def preorder_traverse(node):
    if node is None:
        return
    print("%d" % node.data)
    preorder_traverse(node.next)

def postorder_traverse(node):
    if node is None:
        return
    postorder_traverse(node.next)
    print("%d" % node.data)

if __name__ == '__main__':
    print("preorder traversal")
    preorder_traverse(ll.head)
    print("postorder traversal")
    postorder_traverse(ll.head)
