from singly.linked_list import LinkedList


def test_construction():
    linked_list = LinkedList()
    assert linked_list.head == None
