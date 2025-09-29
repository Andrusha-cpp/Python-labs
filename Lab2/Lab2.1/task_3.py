def find_second(len_, arr):
    first = arr[0]
    second = arr[1]

    for i in range(2, len_):
        if arr[i] > second:
            second = arr[i]
            if arr[i] > first:
                second += first
                first = second - first
                second = second - first

    return second

length = int(input("How many elements do you want to add:"))
a = []
print("Enter the list")
for i in range(0, length):
    a.append(int(input()))

biggest_sec = find_second(length, a)
print(f"Second biggest number {biggest_sec}")