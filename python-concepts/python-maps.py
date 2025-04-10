""" Map: Applies a function to all items in an input list.  """
""" The map() function takes two arguments: a function and an iterable (like a list or tuple). 
    It then applies the function to each element of the iterable and returns an iterator that yields the transformed values. """

def square(x:int):
    return x**2

numbers=[1,2,3,4]
squared_numbers = map(square,numbers)
ans=list(squared_numbers)
print(ans)