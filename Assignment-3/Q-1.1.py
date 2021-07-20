"""
Write a Python Program to implement your own my_reduce() function which works exactly
like Python's built-in function reduce()
"""
def my_reduce(func,iterable,initializer=None):
    """
    :param func: takes function as first argument
    :param iterable: takes iterable object as second argument
    :param initializer: default value is None. (Optional)
    :return: the reduced list according to the function
    """
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for i in it:
        value = func(value,i)
    return value

##Implementation##
l=[1,2,3,4]

def add(x,y):
    return x+y

sum  = my_reduce(add,l)
print("the sum is:",sum)

prod = my_reduce(lambda a,b:a*b,l)
print("The product is:",prod)








