my_list = list(map(int, input().split()))
length = len(my_list)

def add_first_and_last_elements(my_list):
    # 이 함수를 구현해주세요.
    if length == 0:
      return(0)
    elif length == 1:
      return(my_list[0])
    else:
      return(my_list[0] + my_list[length - 1])

print(add_first_and_last_elements(my_list))