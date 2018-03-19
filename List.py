import unittest

#############UnitTests#############

class LinkedListTests(unittest.TestCase):
    def test_empty_list(self):
        linked_list = LinkedList()
        linked_list.reverse()
        values = list(linked_list)
        self.assertListEqual(values, [])

    def test_one_node(self):
        linked_list = LinkedList(Node(1))
        linked_list.reverse()
        values = list(linked_list)
        self.assertListEqual(values, [1])

    def test_multiple_nodes(self):
        linked_list = LinkedList(Node(1, Node(2, Node(3, Node(4)))))
        linked_list.reverse()
        values = list(linked_list)
        self.assertListEqual(values, [4, 3, 2, 1])

    def test_double_reversal(self):
        linked_list = LinkedList(Node(1, Node(2, Node(3, Node(4)))))
        linked_list.reverse()
        linked_list.reverse()
        values = list(linked_list)
        self.assertListEqual(values, [1, 2, 3, 4])


class Node(object):
    def __init__(self, value: int, next_node: "Node" = None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return self.value



class LinkedList(object):
    def __init__(self, head: Node = None):
        self.head = head

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next

    def reverse(self) -> None:
        if self.head is None:
            return 

        previous_node = None
        current_node = self.head
        next_node = current_node.next

        while next_node is not None:
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            next_node = current_node.next

        self.head = current_node
        self.head.next = previous_node


if __name__ == '__main__':
    unittest.main(verbosity=2)


