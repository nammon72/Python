from datetime import datetime

print("----- hello, python! -----")
odd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
right_times_minute = datetime.today().minute
if right_times_minute in odd:
    print('This is times now!')
else:
    print('This is not time now!')
