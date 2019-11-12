def pivot_split(my_list, my_num):
    left = []
    right = []
    for num in my_list:
        if num < my_num:
            left.append(num)
        else:
            right.append(num)

    return [left,right] 

print(pivot_split([12,7,8,15,2,9,11,-7],8))
print(pivot_split([12,7,8,15,2,9,11,-7],1))