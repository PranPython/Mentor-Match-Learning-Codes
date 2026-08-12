while True:
  try:
    a =int(input('Print the first number :'))
    b = int(input('Print the second number :'))
    print(a+b)
    break
  except ValueError:
    print("only print numbers")
