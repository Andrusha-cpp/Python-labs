def list_input():
    length = int(input("How many elements do you want to add:"))
    arr = []
    print("Enter the list")
    for i in range(0, length):
        arr.append(int(input()))

    return arr

list1 = list_input()
list2 = list_input()

set1 = {el for el in list1}
set2 = {el for el in list2}

print(f"Coincidental elements: {set1 & set2 }",
      f"Missing elements in 1st list: {set2 - set1}"
      f"Missing elements in 2nd list: {set1 - set2}"
      f"Elements in 1st and 2nd lists except coincidental: {set1 ^ set2}")
