# Many values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)
print("\n")

# One value to Multiple Variables

x = y = z = "Orange"

print(x)
print(y)
print(z)
print("\n")

# Unpack Collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruit = ["apple", "banana", "mango"]
x, y, z = fruit

print(x)
print(y)
print(z)

# Output Variables

x = "pythone is Awesome"
print('\n')
print(x)
print('\n')

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print("\n")

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
print("\n")

x = 5
y = 10
print(x +y)
print("\n")

x = 5
y = "John"
print(x, y)

'''
x = 5
y = "John"
print(x + y)
Error occurs as one is int and other is str
'''

print("\n")
print('Hello', 'World')