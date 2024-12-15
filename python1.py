import copy

lst1 = [[1,2],[3,4]]
lst2 = [[5,6],[7,8]]

#shallow copy
lst1_copy = copy.copy(lst1)
lst1_copy[0][1] = 7
# print(lst1, '->', lst1_copy)


# deep copy
lst2_copy = copy.deepcopy(lst2)
lst2_copy[0][0] = 10
print(lst2, '->', lst2_copy)

