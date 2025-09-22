string = input("Input string:")

vowels = "aeiouAEIOU" #all the vowels
vowels_set = set() #set to put in it all vowels of the string

for letter in string: #find vowels
    if letter in vowels:
        vowels_set.add(letter)

for el in vowels_set: #remove vowels
    string = string.replace(el, "")

print(string)