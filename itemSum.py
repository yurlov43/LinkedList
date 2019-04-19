from linkedList import Node
from linkedList import LinkedList


def item_sum_of_lists(first_list, second_list):
    third_list = LinkedList()
    if first_list.len() == second_list.len():
        length = first_list.len()
        first_item = first_list.head
        second_item = second_list.head
        for i in range(length):
            third_list.add_in_tail(Node(first_item.value + second_item.value))
            first_item = first_item.next
            second_item = second_item.next
    return third_list


if __name__ == "__main__":
    first_list = LinkedList()
    first_list.add_in_tail(Node(3))
    first_list.add_in_tail(Node(6))
    first_list.add_in_tail(Node(9))
    first_list.add_in_tail(Node(12))
    first_list.print_all_nodes()
    print('\n')
    second_list = LinkedList()
    second_list.add_in_tail(Node(2))
    second_list.add_in_tail(Node(4))
    second_list.add_in_tail(Node(8))
    second_list.add_in_tail(Node(10))
    second_list.print_all_nodes()
    print('\n')
    third_list = LinkedList()
    third_list = item_sum_of_lists(first_list, second_list)
    third_list.print_all_nodes()
