month = int(input("월(month) 를 숫자로 입력해주세요: "))
day = int(input("일(day) 를 숫자로 입력해주세요: "))

month_31 = 1, 3, 5, 7, 8, 10, 12

## 아래 코드를 입력해주세요.
def print_month(month):
  if (1 <= month or month <= 11):
    print(month + 1)
  elif (month == 12):
    print(1)

def print_day(month, day):
  if (month == month_31):
    if (day != 31):
      print(day + 1)
    else:
      print(1)
  elif (month == 2):
    if (day != 28):
      print(day + 1)
    else:
      print(1)
  else:
    if (day != 30):
      print(day + 1)
    else:
      print(1)

print_month(month)
print_day(month, day)