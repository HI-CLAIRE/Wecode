num = [1, 3, 2, 4, 6]

def remove_odd_num(num):
    for i in num[:]:
        if i % 2 == 1:
            num.remove(i)
    print(num)

remove_odd_num(num)