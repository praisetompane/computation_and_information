from bubble_sort import sort


def test_bubble_sort():
    data = [8, 1, 2, 7, 4, 3, 5]
    assert sort(data) == [1, 2, 3, 4, 5, 7, 8]
