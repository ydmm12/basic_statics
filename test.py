import unittest
from models.data_capture import DataCapture
from exceptions.exceptions import NegativeValueException, HigherValueException, TypeErrorException, OrderValueException

class Test(unittest.TestCase):
    negative_error = -2
    type_error = "2"
    higher_error = 20000
    begin = 6
    final = 3
    
    def test(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        self.assertEqual(stats.less(4), 2)
        self.assertEqual(stats.between(3, 6), 4)
        self.assertEqual(stats.greater(4), 2)
        
    def test_error_add(self):
        capture = DataCapture()
        with self.assertRaises(NegativeValueException) as context:
            capture.add(self.negative_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(self.negative_error) + " and need be a positive integer")
        with self.assertRaises(TypeErrorException) as context:
            capture.add(self.type_error)
        self.assertEqual(context.exception.args[0], "The type of the number is: " + str(type(self.type_error))+ " and need be a positive integer")
        with self.assertRaises(HigherValueException) as context:
            capture.add(self.higher_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(self.higher_error)+ " and need be a positive integer less than 1000")
        
    def test_error_less(self):
        capture = DataCapture()
        stats = capture.build_stats()
        with self.assertRaises(NegativeValueException) as context:
            stats.less(self.negative_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(self.negative_error) + " and need be a positive integer")
        with self.assertRaises(NegativeValueException) as context:
            stats.greater(self.negative_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(self.negative_error) + " and need be a positive integer")
        with self.assertRaises(NegativeValueException) as context:
            stats.between(self.negative_error, self.final)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(self.negative_error) + " and need be a positive integer")
        with self.assertRaises(NegativeValueException) as context:
            stats.between(self.begin, self.negative_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(self.negative_error) + " and need be a positive integer")
        
    def test_error_type(self):
        capture = DataCapture()
        stats = capture.build_stats()
        with self.assertRaises(TypeErrorException) as context:
            stats.less(self.type_error)
        self.assertEqual(context.exception.args[0], "The type of the number is: " + str(type(self.type_error))+ " and need be a positive integer")
        with self.assertRaises(TypeErrorException) as context:
            stats.greater(self.type_error)
        self.assertEqual(context.exception.args[0], "The type of the number is: " + str(type(self.type_error))+ " and need be a positive integer")
        with self.assertRaises(TypeErrorException) as context:
            stats.between(self.type_error, self.final)
        self.assertEqual(context.exception.args[0], "The type of the number is: " + str(type(self.type_error))+ " and need be a positive integer")
        with self.assertRaises(TypeErrorException) as context:
            stats.between(self.begin, self.type_error)
        self.assertEqual(context.exception.args[0], "The type of the number is: " + str(type(self.type_error))+ " and need be a positive integer")
        
    def test_error_higher(self):
        capture = DataCapture()
        stats = capture.build_stats()
        with self.assertRaises(HigherValueException) as context:
            stats.less(self.higher_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(self.higher_error)+ " and need be a positive integer less than 1000")
        with self.assertRaises(HigherValueException) as context:
            stats.greater(self.higher_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(self.higher_error)+ " and need be a positive integer less than 1000")
        with self.assertRaises(HigherValueException) as context:
            stats.between(self.higher_error, self.final)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(self.higher_error)+ " and need be a positive integer less than 1000")
        with self.assertRaises(HigherValueException) as context:
            stats.between(self.begin, self.higher_error)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(self.higher_error)+ " and need be a positive integer less than 1000")
        
    def test_error_order(self):
        capture = DataCapture()
        stats = capture.build_stats()
        with self.assertRaises(OrderValueException) as context:
            stats.less(self.begin, self.final)
        self.assertEqual(context.exception.args[0], "The value of the final number is: " + str(self.final)+ " and need be greater than the first number: "+ str(self.begin))
        