while True:
  try:
    a =int(input('Print the first number :'))
    b = int(input('Print the second number :'))
    print(a+b)
    break
  except ValueError:
    print("only print numbers")
try:
  v = int(input("enter a number"))
  x = int(input("Enter a Number"))
  print(v/x)
except TypeError:
  print("cannot add different data types")
except ZeroDivisionError:
  print("Cannot divide the number by 0,Try another Number")
