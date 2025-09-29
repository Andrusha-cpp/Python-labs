string = input("Enter the string:")

words = [word.lower() for word in string.split()]
counter = {}
for word in words:
    if word not in counter:
        counter[word] = 1
    else:
        counter[word] += 1
unique_words = len(counter)

print("Words in string:", counter)
print("Unique words:", unique_words)
