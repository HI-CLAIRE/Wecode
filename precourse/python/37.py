lst1 = list(input())
lst2 = list(input())

def func(lst1, lst2):
    lst1 = lst1 + lst2
    if lst1 != []:
        lst1[0], lst1[-1] = lst1[-1], lst1[0]
    return lst1

print(func(lst1, lst2))