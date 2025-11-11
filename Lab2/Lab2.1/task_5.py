str1 = input("Enter first string:")
str2 = input("Enter second string:")

set1 = {letter for letter in str1}
set2 = {letter for letter in str2}

if len(str1) == len(str2):
    if set1 == set2:
        print("True")
    else:
        print("False")
else:
    print("False")