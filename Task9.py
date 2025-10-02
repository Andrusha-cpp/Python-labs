IP = input("Enter IP-adress: ")

nums = IP.split(".")
if len(nums) != 4:
    print("Incorrect IP-adress")
else:
    nums[1] = int(nums[1])
    nums[2] = int(nums[2])
    nums[3] = int(nums[3])
    nums[4] = int(nums[4])
    if all(0 <= nums <= 255 for num in nums):
        print("Correct IP-adress.")
    else:
        print("Incorrect IP-adress")