# Write your function here
def double_index(lst, index):
    if index >= len(lst):
        return lst
    else:
        new_list = lst[0:index]
    new_list.append(lst[index] * 2)
    new_list += lst[index+1:]
    return new_list


print(double_index([3, 8, -10, 12], 2))
