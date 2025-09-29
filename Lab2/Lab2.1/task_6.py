length = int(input("How many elements do you want to add:"))
arr = []
print("Enter the list")
for i in range(0, length):
    arr.append(int(input()))

set_ = []
for el in arr:
    if el not in set_:
        set_.append(el)

print(set_)
