name = input()
age = int(input())

def check_age(name, age):
    if age < 21:
      return f"Go, home, {name}!"
    elif age >= 21:
      return (f"Nice to meet You, {name}!")

print(check_age(name, age))