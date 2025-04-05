from singly.linked_list import LinkedList
from singly.node import Node


def test_construction():
    linked_list = LinkedList()
    assert linked_list.head == None


def test_insert_at_top():
    linked_list = LinkedList()
    linked_list.insert_at_top(1)
    linked_list.insert_at_top(2)

    assert linked_list.head.data == 2
    assert linked_list.head.next.data == 1


def test_remove_from_top():
    linked_list = LinkedList()
    linked_list.insert_at_top(1)
    linked_list.insert_at_top(2)

    data = linked_list.remove_from_top()
    assert data == 2
    assert linked_list.head.data == 1

    data = linked_list.remove_from_top()
    assert data == 1
    assert linked_list.head == None

    try:
        linked_list.remove_from_top()
    except ValueError as e:
        assert e.args == ("List is empty", )
