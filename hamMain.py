# # Declare a variable and initialize it
# a = 100
# print(a)
#
# # Global vs. local variables in function
# def somefuntion():
# # global a
#     a = 'Xin chao!'
#     print(a)
#
# somefuntion()
# print(a)

# # Declare a number_of_day variable of type integer is 10
# number_of_day = 10
#
# # Declare a distance variable of type float is 20.5
# distance = 20.5
#
# # Declare a greeting variable of type string is "Hello nammon72"
# greeting = "Hello nammon72"
#
# # Declare a is_student variable of type boolean is True
# is_student = True
#
# print(number_of_day, "\n", distance, "\n", greeting, "\n", is_student)

# a = 0
# s = 0
# print('Những số chẵn trong khoảng từ 0 -> 100 là:')
# for a in range(101):
#     if a % 2 == 0:
#         print(a)
#     else:
#         print(' ')

# number_of_day = 10
# data_type_of_number_of_day = type(number_of_day)
# print(data_type_of_number_of_day)
# distance = 20.5
# data_type_of_distance = type(distance)
# print(data_type_of_distance)
# greeting = "Xin chao!"
# data_type_of_greeting = type(greeting)
# print(data_type_of_greeting)
# is_student = True
# data_type_of_is_student = type(is_student)
# print(data_type_of_is_student)

# # yeu cau user nhap thong tin tu ban phim
# input_data = input("Enter your name: ")
#
# # lay kieu du lieu cua input_data
# data_type_input_data = type(input_data)
#
# print("---------------------------------")
# print("Your data type input is: ", data_type_input_data, input_data)
#
# a_long_string = '''Xin chao cac ban!
# minh la Nam
# Hom nay la cuoi tuan, troi nang rat dep'''
# print(a_long_string)
# print(input_data + a_long_string)

# name = "Nam"
# guy = "ban"
# full = "Chao mung %s %s den voi khoa hoc python co ban" %(guy, name)
# print(full)

# ages = [5, 12, 17, 18,24, 32]
#
# def myFunc(x):
#     if x < 18:
#         return False
#     else:
#         return True
# adults = filter(myFunc, ages)
#
# for x in adults:
#     print(x)

try:
    number_of_items = int(input("Enter the number of items in the list:"))
    if number_of_items <= 0:
        exit()
except:
    print('type of number is integer!')
    exit()
list = []

for i in range(number_of_items):
    list.append(input('Enter the number of %d: ' % (i+1)))

number_of_filter = int(input("Enter number of filter: "))
def filterNum(number_of_filter):
    if number_of_filter not in list:
        return False
    else:
        return True
number_of_k = filter(filterNum, list)

for number_of_filter in list:
    print(number_of_filter)