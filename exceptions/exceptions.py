class NegativeValueException(Exception):
    pass

class TypeErrorException(Exception):
    pass

class HigherValueException(Exception):
    pass

class OrderValueException(Exception):
    pass

def check_integers(f):
    def wrapper(*args, **kwargs):
        first_value = True
        for arg in args[1:]:
            if type(arg) is not int:
                raise TypeErrorException("The type of the number is: " + str(type(arg))+ " and need be a positive integer")
            elif arg < 0:
                raise NegativeValueException("The value of the number is: " + str(arg) + " and need be a positive integer")
            elif arg>=1000:
                raise HigherValueException("The value of the number is: " + str(arg)+ " and need be a positive integer less than 1000")
            if not first_value:
                if args[2] < args[1]:
                    raise OrderValueException("The value of the final number is: " + str(args[2])+ " and need be greater than the first number: "+ str(args[1]))
            first_value = False
        result = f(*args, **kwargs)
        return result
    return wrapper