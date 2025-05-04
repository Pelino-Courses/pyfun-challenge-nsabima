
def add(*args):
    return sum(args)
def substract(*args):
    if len(args) < 2:
        raise ValueError("substraction needs two numbers.")
    result=args[0]
    for num in args[1:]:
        result-=num
    return result
def multiply(*args):
    result=1
    for num in args:
        result*=num
    return result
def divide(*args):
    if len (args)<2:
        raise ValueError("divide needs at least two numbers.")
    result=args[0]
    for num in args[1:]:
        if num== 0:
            raise ZeroDivisionError("cannot divide by zero")
        result /=num
    return result
