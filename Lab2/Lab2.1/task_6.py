arr = [float(x) for x in input("Enter the array: ").split()]

set_ = []
for el in arr:
    if el not in set_:
        set_.append(el)

print(set_)
