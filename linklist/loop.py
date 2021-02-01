#!/usr/bin/python3

from linklist import *

def is_loop(head):
    index = 0
    p1 = head
    p2 = head
    while p1 is not None and p2 is not None:
        index += 1

        n = p1.next
        if n is not None:
            p1 = n.next

        p2 = p2.next

        if p1 == p2:
            print("loop exists because of p1==p2, index=%d" % index)
            return True

    return False

if __name__ == '__main__':
    ll = CreateLinkList(8)

    tail = ll.tail()
    node = ll.step(4)
    print(node.data)
    tail.next = node

    is_loop(ll.head)

