first_list = ['d','a', 'c', 'b', 'e']
second_list = [1 , 2 , 3 , 4 , 5]

first_list.sort()
first_list.reverse()

second_list.reverse()

print(first_list[2:] + second_list[2:])