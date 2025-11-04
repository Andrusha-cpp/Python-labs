array = list(map(float, input("Enter the array: ").split()))
array2 = [float(x) if '.' in x else int(x) for x in input("Enter the array:").split()]
print(array)
print(array2)
print(array2[3] + array2[4])