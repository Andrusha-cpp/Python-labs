from src.Task2 import unique_elements

def test_simple_list():
    assert unique_elements([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_repeat_values():
    assert unique_elements([1, 2, 4, 3, 1]) == [1, 2, 4, 3]

def test_nested_list():
    assert unique_elements([1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]) == [1, 2, 3, 4, 5, 6, 7, 10, 8, 9]