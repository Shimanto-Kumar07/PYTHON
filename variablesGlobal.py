x = "awesome"
def myFunc():
    print("Python is " + x)

myFunc()

# Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myFunc():
    x = "fantastic"
    print("Python is " + x)

myFunc()

print("Python is " + x)

# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)