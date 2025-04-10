""" Lambda functions are small anonymous functions defined using the lambda keyword.  """

def add(x:int,y:int)->int:
    return x+y

add_lambda = lambda x,y: x+y


a=1
b=2
ans=add(a,b)
print(add_lambda(a,b))