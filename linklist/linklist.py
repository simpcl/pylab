#!/usr/bin/python3

def print_data(node):
    print(node.data, end=',')

def print_node(node):
    print(node, end=',')

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

    def head(self):
        return self.head

    def tail(self):
        nn = self.head
        while nn.next is not None:
            nn = nn.next
        return nn

    def step(self, num):
        nn = self.head
        i = 0
        while nn is not None:
            nn = nn.next
            i += 1
            if i >= num:
                return nn
        return None

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
            callback(nn)
            nn = nn.next

    def show(self):
        self.apply_for_all(print_data)
        print('$')

    def show_node(self):
        self.apply_for_all(print_node)
        print('$')

def CreateLinkList(num):
    ll = LinkList(Node(0))
    node = ll.head
    for i in range(1, num): 
        node.next = Node(i)
        node = node.next
    return ll

if __name__ == '__main__':
    ll = LinkList(Node(1))
    ll.prepend(Node(0))
    ll.append(Node(2))
    for i in range(8):
        ll.append(Node(i+3))
    ll.show()

