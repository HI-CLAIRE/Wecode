def find_divisor(num):
    x = 2
    while x <= num:
        if num % x == 0:
            return x
            break
        x += 1
print(find_divisor(15))