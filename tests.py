import unittest
from linkedList import Node
from linkedList import LinkedList


class LinkedListTestsSample(unittest.TestCase):
    def test_delete_first_item(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(35))
        s_list.delete(17, False)
        self.assertEqual(s_list.head.value, 35)
        self.assertEqual(s_list.tail.value, 35)

    def test_delete_last_item(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(35))
        s_list.delete(35, False)
        self.assertEqual(s_list.head.value, 17)
        self.assertEqual(s_list.tail.value, 17)

    def test_delete_middle_item(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(35))
        s_list.add_in_tail(Node(88))
        s_list.delete(35, False)
        self.assertEqual(s_list.head.value, 17)
        self.assertEqual(s_list.tail.value, 88)

    def test_delete_only_item_in_list(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(35))
        s_list.delete(35, False)
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)

    def test_delete_item_from_empty_list(self):
        s_list = LinkedList()
        n1 = Node(35)
        s_list.delete(n1, False)
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)

    def test_delete_all_items(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(35))
        s_list.add_in_tail(Node(17))
        s_list.delete(17, True)
        self.assertEqual(s_list.head.value, 35)
        self.assertEqual(s_list.tail.value, 35)

    def test_delete_all_items_get_an_empty_list(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(17))
        s_list.delete(17, True)
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)

    def test_delete_all_items_from_empty_list(self):
        s_list = LinkedList()
        n1 = Node(35)
        s_list.delete(n1, True)
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)

    def test_clean_all_content(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(35))
        s_list.add_in_tail(Node(99))
        s_list.clean()
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)

    def test_find_all_items(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(35))
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(99))
        matches_list = s_list.find_all(17)
        self.assertEqual(len(matches_list), 2)
        for item in matches_list:
            self.assertEqual(item.value, 17)

    def test_not_find_all_items(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(35))
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(99))
        matches_list = s_list.find_all(6)
        self.assertEqual(len(matches_list), 0)
        self.assertEqual(matches_list, [])

    def test_find_all_items_in_list_with_one_item(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(17))
        matches_list = s_list.find_all(17)
        self.assertEqual(len(matches_list), 1)
        for item in matches_list:
            self.assertEqual(item.value, 17)

    def test_find_all_in_empty_list(self):
        s_list = LinkedList()
        matches_list = s_list.find_all(17)
        self.assertEqual(len(matches_list), 0)
        for item in matches_list:
            self.assertEqual(item, None)

    def test_find_item(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(35))
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(99))
        self.assertEqual(s_list.find(17).value, 17)
        self.assertEqual(s_list.find(17), s_list.head)

    def test_not_find_item(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(35))
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(99))
        self.assertEqual(s_list.find(6), None)

    def test_find_item_in_list_with_one_item(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(17))
        self.assertEqual(s_list.find(17).value, 17)
        self.assertEqual(s_list.find(17), s_list.head)

    def test_find_in_empty_list(self):
        s_list = LinkedList()
        self.assertEqual(s_list.find(17), None)

    def test_list_length(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(35))
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(99))
        self.assertEqual(s_list.len(), 4)

    def test_empty_list_length(self):
        s_list = LinkedList()
        self.assertEqual(s_list.len(), 0)

    def test_insert_item_list_is_None(self):
        s_list = LinkedList()
        s_list.insert(None, Node(5))
        self.assertEqual(s_list.head.value, 5)

    def test_insert_item(self):
        s_list = LinkedList()
        n1 = Node(17)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(Node(35))
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(99))
        n2 = Node(5)
        s_list.insert(n1, n2)
        self.assertEqual(s_list.head.next, n2)

    def test_insert_item_at_end_of_list(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(17))
        s_list.add_in_tail(Node(35))
        s_list.add_in_tail(Node(17))
        n1 = Node(99)
        s_list.add_in_tail(n1)
        n2 = Node(5)
        s_list.insert(n1, n2)
        self.assertEqual(s_list.tail, n2)


if __name__ == '__main__':
    unittest.main()
