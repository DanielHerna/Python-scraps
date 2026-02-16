''' lambda arguments: expression 
it is better to use as an anonymus function inside another function

'''

def num(x):
    return lambda a: a*x

doubler = num(2) # This will assig the lambda value to 2
print(doubler(20))


'''  labmda will multiply the number x by a
to define a I need to assig lambda to a function since it is an annonymous one 


'''
