
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

    print("preorder traversal")
    preorder_traverse(node1)
    print("postorder traversal")
    postorder_traverse(node1)
