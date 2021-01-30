#!/usr/bin/python

# BFT: BreadthFirstTraversal
# DFT: DepthFirstTraversal


class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def BFT(self):
        l = []
        l.append(self)
        while len(l) > 0:
            bt = l.pop(0)
            if bt:
                print(bt.data)
                l.append(bt.left)
                l.append(bt.right)

    def PreOrderDFT(self):
        print(self.data)
        if self.left:
            self.left.PreOrderDFT()
        if self.right:
            self.right.PreOrderDFT()

    def PreOrderDFTWithStack(self):
        l = []
        l.append(self)
        while len(l) > 0:
            node = l.pop()
            print(node.data)
            if node.right:
                l.append(node.right)
            if node.left:
                l.append(node.left)

    def InOrderDFT(self):
        if self.left:
            self.left.InOrderDFT()
        print(self.data)
        if self.right:
            self.right.InOrderDFT()

    def InOrderDFTWithStack(self):
        l = []
        l.append(self)
        node = self
        while len(l) > 0:
            while node.left:
                l.append(node.left)
                node = node.left

            node = l.pop()
            print(node.data)
            if node.right:
                node = node.right
                l.append(node)

    def AfterOrderDFT(self):
        if self.left:
            self.left.AfterOrderDFT()
        if self.right:
            self.right.AfterOrderDFT()
        print(self.data)

    def AfterOrderDFTWithStack(self):
        pass

def CreateTree():
    bt1 = BinaryTree(2, BinaryTree(1), BinaryTree(3))
    bt2 = BinaryTree(6, BinaryTree(5), BinaryTree(7))
    bt = BinaryTree(4, bt1, bt2)
    return bt

if __name__ == '__main__':
    tree = CreateTree()
    print('--------')
    tree.BFT()
    print('--------')
    tree.PreOrderDFT()
    tree.PreOrderDFTWithStack()
    print('--------')
    tree.InOrderDFT()
    tree.InOrderDFTWithStack()
    print('--------')
    tree.AfterOrderDFT()
    tree.AfterOrderDFTWithStack()

