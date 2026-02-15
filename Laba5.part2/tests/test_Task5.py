from src.Task5 import merge_dicts

dict1 = {"a": 1, "b": {"c": 1, "f": 4}}
dict2 = {"d": 1, "b": {"c": 2, "e": 3}}

def test_same_dicts():
    assert merge_dicts(dict1, dict1) == {"a": 1, "b": {"c": 1, "f": 4}}

def test_nested_dicts():
    assert merge_dicts(dict1, dict2) == {"a": 1, "b": {"c": 2, "d": 3, "f": 4}, "e": 1}