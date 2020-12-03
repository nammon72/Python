# Declare a variable and initialize it
a = 100
print(a)

# Global vs. local variables in function
def somefuntion():
# global a
    a = 'Xin chao!'
    print(a)

somefuntion()
print(a)
