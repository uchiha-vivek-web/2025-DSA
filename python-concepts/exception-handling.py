""" Exception Handling """

""" Exceptions are error that occur during program execution """
""" Finally block will always run irrespective of what exception occurs  """

try:
    x=10/0
except ZeroDivisionError :
    print('Cannot divide by Zero')
else:
    print('Divison successfull')
finally:
    print('The program will always run')