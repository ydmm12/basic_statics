import unittest
from models.data_capture import DataCapture
from exceptions.exceptions import NegativeValueException, HigherValueException, TypeErrorException, OrderValueException

class Test(unittest.TestCase):
    
    def test_1(self):
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
        
    def test_add_negative_error(self):
        capture = DataCapture()
        add = -3
        with self.assertRaises(NegativeValueException) as context:
            capture.add(add)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(add) + " and need be a positive integer")
        
    def test_add_type_error(self):
        capture = DataCapture()
        add = "3"
        with self.assertRaises(TypeErrorException) as context:
            capture.add(add)
        self.assertEqual(context.exception.args[0], "The type of the number is: " + str(type(add))+ " and need be a positive integer")
        
    def test_add_higher_error(self):
        capture = DataCapture()
        add = 9999
        with self.assertRaises(HigherValueException) as context:
            capture.add(add)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(add)+ " and need be a positive integer less than 1000")
        
    def test_less_negative_error(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        less = -2
        with self.assertRaises(NegativeValueException) as context:
            stats.less(less)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(less) + " and need be a positive integer")
        
    def test_less_type_error(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        less = "2"
        with self.assertRaises(TypeErrorException) as context:
            stats.less(less)
        self.assertEqual(context.exception.args[0], "The type of the number is: " + str(type(less))+ " and need be a positive integer")
        
    def test_less_higher_error(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        less = 20000
        with self.assertRaises(HigherValueException) as context:
            stats.less(less)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(less)+ " and need be a positive integer less than 1000")
        
    def test_greater_negative_error(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        greater = -2
        with self.assertRaises(NegativeValueException) as context:
            stats.greater(greater)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(greater) + " and need be a positive integer")
        
    def test_greater_type_error(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        greater = "2"
        with self.assertRaises(TypeErrorException) as context:
            stats.greater(greater)
        self.assertEqual(context.exception.args[0], "The type of the number is: " + str(type(greater))+ " and need be a positive integer")
        
    def test_greater_higher_error(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        greater = 20000
        with self.assertRaises(HigherValueException) as context:
            stats.greater(greater)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(greater)+ " and need be a positive integer less than 1000")
        
    def test_between_negative_error_begin(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        begin = -2
        final = 9
        with self.assertRaises(NegativeValueException) as context:
            stats.between(begin, final)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(begin) + " and need be a positive integer")
        
    def test_between_type_error_begin(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        begin = "2"
        final = 9
        with self.assertRaises(TypeErrorException) as context:
            stats.between(begin, final)
        self.assertEqual(context.exception.args[0], "The type of the number is: " + str(type(begin))+ " and need be a positive integer")
        
    def test_between_higher_error_begin(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        begin = 20000
        final = 30000
        with self.assertRaises(HigherValueException) as context:
            stats.less(begin, final)
        self.assertEqual(context.exception.args[0], "The value of the number is: " + str(begin)+ " and need be a positive integer less than 1000")
        
    def test_between_order_error(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        begin = 6
        final = 3
        with self.assertRaises(OrderValueException) as context:
            stats.less(begin, final)
        self.assertEqual(context.exception.args[0], "The value of the final number is: " + str(final)+ " and need be greater than the first number: "+ str(begin))
        