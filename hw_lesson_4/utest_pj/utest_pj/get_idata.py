f_lst = [4, 8, -5, 4, 9, 2]


def def_index2(arr):
    min_val = arr[0]
    min_ind = 0
    for i in range(len(arr)):
        if min_val > arr[i]:
            min_val = arr[i]
            min_ind = i
    return min_ind


# print(def_index2(f_lst))
