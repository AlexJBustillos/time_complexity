# Given two arrays of integers, return an array that contains just the elements that are present in both input arrays. The input arrays are not guaranteed to be sorted, but any given element will only appear once in a given input array.

# Sample 1: intersection([0, 1, 4, 5, 8], [0, 2, 7, 9, 4]) -> [0, 4]
# quadriatic
def intersection(arr1, arr2):
    new_list = []
    if arr1 == [] or arr2 == []:
        new_list = []
    else:
        for i in arr1:
            for j in arr2:
                if i == j:
                    new_list.append(i)
    return new_list
# quadriatic
def inter(arr1, arr2):
    arr3 = []

    for i in arr1:
        if i in arr2:
            arr3.append(i)

    return arr3
# linear time complexity
def int1(arr1, arr2):
    dictionary = {}
    arr3 = []
    for a in arr1:
        dictionary[str(a)] = 'bingo'
    for b in arr2:
        if str(b) in dictionary:
            arr3.append(b)


    return arr3
        

# print(int1([3,4], [1,2,3]))
# print(int1([5,4,10,100], [1,500,30]))
# print(int1([1, 20, 200, 4], [2, 20, 200]))
# print(int1([34,55], [5, 55, 56, 57]))  
# Linear time complexity
def milan(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    return list(set1 & set2)


print(milan([3,4], [1,2,3]))
print(milan([5,4,10,100], [1,500,30]))
print(milan([1, 20, 200, 4], [2, 20, 200]))
print(milan([34,55], [5, 55, 56, 57]))        

# print(intersection([3,4], [1,2,3]))
# print(intersection([5,4,10,100], [1,500,30]))
# print(intersection([1, 20, 200, 4], [2, 20, 200]))
# print(intersection([34,55], [5, 55, 56, 57]))




