my_list = [1, 2, 3, 4, 5, 6]

def convert_list_to_list_of_tuples(my_list):
# 함수를 완성해 주세요.
  new = []
  tup1 = tuple(my_list[:2])
  tup2 = tuple(my_list[2:4])
  tup3 = tuple(my_list[4:])
  new.append(tup1)
  new.append(tup2)
  new.append(tup3)
  print(new)

convert_list_to_list_of_tuples(my_list)