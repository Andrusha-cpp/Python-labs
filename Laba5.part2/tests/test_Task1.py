from src.Task1 import words_counter

def test_zero_spaces():
    assert words_counter("HelloWorld!") == 1

def test_one_space():
    assert words_counter("Hello World!") == 2

def test_many_spaces():
    assert words_counter("Hello Beutiful World !") == 4

def test_no_words():
    assert words_counter("") == 0

def test_only_spaces():
    assert words_counter("   ") == 0