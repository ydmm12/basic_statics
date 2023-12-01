from exceptions.exceptions import check_integers

class Stats:
    """Class to get the statistics of the data received."""
    def __init__(self, data: list):
        """When the object is initialized, it fills all the values with the sum of the previous numbers.

        Args:
            data (list): The data with the numeric values per position.
        """
        for number in range(1,len(data)):
            data[number]+=data[number-1]
        self.data = data
            
    @check_integers
    def less(self, number: int) -> int:
        """Function to get all numbers before the value.

        Args:
            number (int): Numeric value to get all the numbers before, the number must always be between 1 and 999.

        Returns:
            int: Number of values.
        """
        return self.data[number-1]
            
    @check_integers
    def greater(self, number:int) -> int:
        """Function to get all numbers after the value.

        Args:
            number (int): Numeric value to get all the numbers after, the number must always be between 1 and 999.

        Returns:
            int: Number of values.
        """
        return self.data[-1] - self.data[number]
            
    @check_integers
    def between(self, begin:int, finish:int) -> int:
        """Function to get all numbers between two values with these values included.

        Args:
            begin (int): Numeric value with the start of the count, the number must always be between 1 and 999 and less than the finish value.
            finish (int): Numeric value with the end of the count, the number must always be between 1 and 999 and greater than the begin value.

        Returns:
            int: Number of values.
        """
        dif = self.data[begin-1] if begin != 0 else 0
        return self.data[finish] - dif