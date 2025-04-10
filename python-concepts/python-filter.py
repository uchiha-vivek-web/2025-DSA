""" filter() helps you extract elements from an iterable based on a specific condition.  """


def is_even(num):
    return num%2==0

numbers=[1,2,3,4,5,6]
even_numbers  = filter(is_even,numbers)
ans=list(even_numbers)
print(ans)