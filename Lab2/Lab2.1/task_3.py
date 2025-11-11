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

arr = [float(x) for x in input("Enter the array: ").split()]
length = len(arr)

biggest_sec = find_second(length, arr)
print(f"Second biggest number is {biggest_sec}")