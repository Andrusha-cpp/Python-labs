def merge_sorted_list(list1, list2):
    merge_list = []
    i = 0
    j = 0

    length1 = len(list1)
    length2 = len(list2)

    while i < length1 and j < length2: #add elements from list1 and list2 by comparing them
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i += 1
        elif list1[i] == list2[j]:
            merge_list.append(list1[i])
            i += 1
            j += 1
        else:
            merge_list.append(list2[j])
            j += 1

    if i < length1:
        while i < length1: #add elements if we finished list2
            merge_list.append(list1[i])
            i += 1

    if j < length2:
        while j < length2: #add elements if we finished list1
            merge_list.append(list2[j])
            j += 1

    return merge_list

list1 = [1, 3, 5, 6, 7, 8, 10]
list2 = [1, 2, 6, 8, 9]

print(merge_sorted_list(list1, list2))