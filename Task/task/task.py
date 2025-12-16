def shortest_word(string):
    words = string.split()
    shortest_len = len(words[0])
    for word in words:
        if len(word) <= shortest_len:
            shortest_len = len(word)
            shortest = word
    return shortest