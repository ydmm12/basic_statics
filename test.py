import unittest
from models.data_capture import DataCapture
from exceptions.exceptions import NegativeValueException, HigherValueException, TypeErrorException, OrderValueException

class Test(unittest.TestCase):
    
    def test(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        negative_error = -2
        type_error = "2"
        higher_error = 20000
        begin = 6
        final = 3
        with self.assertRaises(NegativeValueException) as context:
            capture.add(negative_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(negative_error) + " and need be a positive integer")
        with self.assertRaises(TypeErrorException) as context:
            capture.add(type_error)
        self.assertEqual(context.exception.args[0], "The type of the number is: " + str(type(type_error))+ " and need be a positive integer")
        with self.assertRaises(HigherValueException) as context:
            capture.add(higher_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(higher_error)+ " and need be a positive integer less than 1000")
        stats = capture.build_stats()
        with self.assertRaises(NegativeValueException) as context:
            stats.less(negative_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(negative_error) + " and need be a positive integer")
        with self.assertRaises(NegativeValueException) as context:
            stats.greater(negative_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(negative_error) + " and need be a positive integer")
        with self.assertRaises(NegativeValueException) as context:
            stats.between(negative_error, final)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(negative_error) + " and need be a positive integer")
        with self.assertRaises(NegativeValueException) as context:
            stats.between(begin, negative_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(negative_error) + " and need be a positive integer")
        with self.assertRaises(TypeErrorException) as context:
            stats.less(type_error)
        self.assertEqual(context.exception.args[0], "The type of the number is: " + str(type(type_error))+ " and need be a positive integer")
        with self.assertRaises(TypeErrorException) as context:
            stats.greater(type_error)
        self.assertEqual(context.exception.args[0], "The type of the number is: " + str(type(type_error))+ " and need be a positive integer")
        with self.assertRaises(TypeErrorException) as context:
            stats.between(type_error, final)
        self.assertEqual(context.exception.args[0], "The type of the number is: " + str(type(type_error))+ " and need be a positive integer")
        with self.assertRaises(TypeErrorException) as context:
            stats.between(begin, type_error)
        self.assertEqual(context.exception.args[0], "The type of the number is: " + str(type(type_error))+ " and need be a positive integer")
        with self.assertRaises(HigherValueException) as context:
            stats.less(higher_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(higher_error)+ " and need be a positive integer less than 1000")
        with self.assertRaises(HigherValueException) as context:
            stats.greater(higher_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(higher_error)+ " and need be a positive integer less than 1000")
        with self.assertRaises(HigherValueException) as context:
            stats.between(higher_error, final)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(higher_error)+ " and need be a positive integer less than 1000")
        with self.assertRaises(HigherValueException) as context:
            stats.between(begin, higher_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(higher_error)+ " and need be a positive integer less than 1000")
        with self.assertRaises(OrderValueException) as context:
            stats.less(begin, final)
        self.assertEqual(context.exception.args[0], "The value of the final number is: " + str(final)+ " and need be greater than the first number: "+ str(begin))
        self.assertEqual(stats.less(4), 2)
        self.assertEqual(stats.between(3, 6), 4)
        self.assertEqual(stats.greater(4), 2)