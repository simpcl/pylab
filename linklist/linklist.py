#!/usr/bin/python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self, node):
        if node:
            self.head = node
        else:
            self.head = Node()

    def prepend(self, node):
        if not node.next:
            node.next = self.head
            self.head = node

    def append(self, node):
        nn = self.head
        while nn.next:
            nn = nn.next
        nn.next = node

    def apply_for_all(self, callback):
        nn = self.head
        while nn:
            callback(nn.data)
            nn = nn.next

    def reverse(self):
        head = None
        while self.head:
            node = self.head
            self.head = self.head.next
            node.next = head
            head = node
        self.head = head

def print_data(data):
    print(data)

if __name__ == '__main__':
    ll = LinkList(Node(1))
    ll.prepend(Node(0))
    ll.append(Node(2))
    for i in range(8):
        ll.append(Node(i+3))
    ll.apply_for_all(print_data)
    ll.reverse()
    ll.apply_for_all(print_data)
