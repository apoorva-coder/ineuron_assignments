"""
Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()
"""
def my_filter(func,iterable):
    """
    :param func: takes a function as argument
    :param iterable: iterables or iterator
    :return: the my_filter object
    """
    m=[]
    if func is not None:
        for i in iterable:
            if func(i):
                yield i

    else:
        for i in iterable:
            if i:
                yield i
    return m

####Implementation - external function ####

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = my_filter(myFunc, ages)
print(list(adults))

### Implementation - Lambda function ###

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

filter_object = my_filter(lambda s: s[0] == "A", fruit)
print(list(filter_object))