from datetime import date

name = input('What is your name?\n')
year_birth = int(input('What is your year birthday?\n'))
favorite_color = input('What is your favorite color?\n')

today = date.today()
year_now = int(today.strftime("%Y"))

your_old = year_now - year_birth

print('Hi, '+name)
print('You are '+str(your_old))
print('Your favorite color is '+favorite_color)