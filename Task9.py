IP = input("Enter IP-adress: ")

nums = IP.split(".")
if len(nums) != 4:
    print("Incorrect IP-adress")
else:
    for num in nums:
        num = int(num)
    if all(0 <= nums <= 255 for num in nums):
        print("Correct IP-adress.")
    else:
        print("Incorrect IP-adress")