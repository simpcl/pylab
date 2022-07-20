#!/usr/bin/python3

from linklist import *

def is_cross(head1, head2):
    tail1 = head1
    tail2 = head2

    while tail1.next is not None:
        tail1 = tail1.next

    while tail2.next is not None:
        tail2 = tail2.next

    #print(tail1)
    #print(tail2)
    if tail1 == tail2:
        return True
    else:
        return False


def find_cross_node(head1, head2):
    count1 = 0
    tail1 = head1
    while tail1.next is not None:
        tail1 = tail1.next
        count1 += 1

    count2 = 0
    tail2 = head2
    while tail2.next is not None:
        tail2 = tail2.next
        count2 += 1

    if tail1 != tail2:
        return None

    tail1 = head1
    tail2 = head2
    if count1 > count2:
        gap = count1 - count2
        while gap > 0:
            tail1 = tail1.next
            gap -= 1
    elif count1 < count2:
        gap = count2 - count1
        while gap > 0:
            tail2 = tail2.next
            gap -= 1
    
    while tail1 is not None or tail2 is not None:
        if tail1 == tail2:
            return tail1
        tail1 = tail1.next
        tail2 = tail2.next

    return None


if __name__ == '__main__':
    ll1 = CreateLinkList(8)
    ll2 = CreateLinkList(6)

    node = ll1.step(3)
    tail = ll2.tail()
    tail.next = node
    print("node: ", node)

    ll1.show_node()
    ll2.show_node()

    crossed = is_cross(ll1.head, ll2.head)
    if crossed:
        print("crossed: true")
    else:
        print("crossed: false")
    print("cross node: ", find_cross_node(ll1.head, ll2.head))

