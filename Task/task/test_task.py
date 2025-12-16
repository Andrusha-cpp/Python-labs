from task import shortest_word

def test_one_word():
    assert shortest_word("short") == "short"

def test_some_words():
    assert shortest_word("short word in tests") == "in"

def test_same_len_word():
    assert shortest_word("short sword") == "sword"

def test_same_word():
    assert shortest_word("short short") == "short"

def test_signd():
    assert shortest_word("short, word not. ") == "not."