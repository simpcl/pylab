#!/usr/bin/python


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def is_loop(node):

    index = 0
    p1 = node
    p2 = node
    while p1 is not None and p2 is not None:
        index += 1

        n = p1.next
        if n is not None:
            p1 = n.next

        p2 = p2.next

        if p1 == p2:
            print "loop exists because of p1 == p2, index=", index
            return True

    return False

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node3

    is_loop(node1)


