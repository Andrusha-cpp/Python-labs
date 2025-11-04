list1 = [float(x) for x in input("Enter the array: ").split()]
list2 = [float(x) for x in input("Enter the array: ").split()]

set1 = {el for el in list1}
set2 = {el for el in list2}

print(f"Coincidental elements: {set1 & set2}\n",
      f"Missing elements in 1st list: {set2 - set1}\n"
      f"Missing elements in 2nd list: {set1 - set2}\n"
      f"Elements in 1st and 2nd lists except coincidental: {set1 ^ set2}\n")
