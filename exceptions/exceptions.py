class NegativeValueException(Exception):
    """Exception when receive a non-positive integer."""
    pass

class TypeErrorException(Exception):
    """Exception when receive an input with a different data type than int."""
    pass

class HigherValueException(Exception):
    """Exception when receive an integer greater than 999."""
    pass

class OrderValueException(Exception):
    """Exception when the first number in the between function is greather than the second."""
    pass

def check_integers(f):
    def wrapper(*args, **kwargs):
        def check_value(arg):
            if type(arg) is not int:
                raise TypeErrorException("The type of the number is: " + str(type(arg))+ " and need be a positive integer")
            elif arg <= 0:
                raise NegativeValueException("The value of the number is: " + str(arg) + " and need be a positive integer")
            elif arg>=1000:
                raise HigherValueException("The value of the number is: " + str(arg)+ " and need be a positive integer less than 1000")
        check_value(args[1])
        if len(args) == 3:
            check_value(args[2])
            if args[2] < args[1]:
                raise OrderValueException("The value of the final number is: " + str(args[2])+ " and need be greater than the first number: "+ str(args[1]))
        result = f(*args, **kwargs)
        return result
    return wrapper