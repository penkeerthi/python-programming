def reverse_list(my_list):
    result = []
    idx = len(my_list) - 1
    while idx >= 0:
        result.append(my_list[idx])
        idx -= 1
    return result



#calling reverse_string
print (reverse_list([1,2,3,4,5]))

new_list = reverse_list(['a','b','c','d','e'])

print(new_list)

classmates = ['emma','chizea','daniela']

print(reverse_list(classmates))


