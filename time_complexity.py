# 0(n) linear time complexity
def linear_example(list):
    for el in list:
        print(el)

# O(1) constant time complexity
def constant_example(list):
    print(list[0])

# logarithmic time complexity O(log(n))
def logarithmic_example(list):
    while len(list) > 1:
        list = list[1:len(list) / 2]
    
    print('Done!')

