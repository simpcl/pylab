#!/usr/bin/python3

from linklist import *

def reverse(ll):
    head = ll.head
    newhead = None
    node = None
    while head is not None:
        node = head
        head = head.next
        node.next = newhead
        newhead = node
    ll.head = newhead

#def create_linklist():
#    ll = LinkList(Node(0))
#    node = ll.head
#    for i in range(1, 8):
#        node.next = Node(i)
#        node = node.next
#    return ll

if __name__ == '__main__':
    ll = CreateLinkList(8)
    ll.show()
    reverse(ll)
    ll.show()
