from src.Task4 import string_comparassion

str1 = "listen"
str2 = "silent"
str3 = "listent"
str4 = "faculty"

def test_same_word():
    assert string_comparassion(str1, str1) == True

def test_annograms():
    assert string_comparassion(str1, str2) == True

def test_more_letters():
    assert string_comparassion(str1, str3) == False

def test_not_annograms():
    assert string_comparassion(str1, str4) == False 