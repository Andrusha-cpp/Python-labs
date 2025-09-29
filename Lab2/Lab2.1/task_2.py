numbers = input("Enter numbers: ")

numbers = numbers.split()
arr = []
for el in numbers:
    if '.' in el:
        arr = float(el)
    else:
        arr = int(el)
print(arr)

#print unique numbers
unique_numbers = []
for el in arr:
    if el not in unique_numbers:
        unique_numbers.append(el)
    else:
        unique_numbers.remove(el)
print(f"Unique numbers: {unique_numbers}")

#print not unique numbers
print("Not unique numbers:", end=" ")
for el in arr:
    if el not in unique_numbers:
        print(el, end=" ")

# print even numbers
print("\nEven numbers:", end=" ")
for el in arr:
    if el % 2 == 0:
        print(el, end=" ")

# print odd numbers
print("\nOdd numbers:", end=" ")
for el in arr:
    if el % 2 != 0:
        print(el, end=" ")

# print negative numbers
print("\nNegative numbers:", end=" ")
for el in arr:
    if el < 0:
        print(el, end=" ")

# print float numbers
print("\nFloat numbers:", end=" ")
for el in arr:
    if type(el) == float:
        print(el, end=" ")

# print summ of numbers mutiple to 5
summ = 0
for el in arr:
    if el % 5 == 0:
        summ += el
print(f"Summ of numbers mutiple to 5: {summ}")

#print the biggest number
max_num = arr[0]
for el in arr:
    if max_num < el:
        max_num = el
print(f"Maximum number: {max_num}")

#print the lowest number
min_num = arr[0]
for el in arr:
    if min_num < el:
        min_num = el
print(f"Maximum number: {min_num}")