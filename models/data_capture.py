from models.stats import Stats
from exceptions.exceptions import check_integers

class DataCapture:
    """Class to get the data and send it to be processed, when it's initialized create a list with all the values at zero."""
    data = [0] * 1000
    
    @check_integers
    def add(self, number: int):
        """Function to get a new value and add it to the position in the list.

        Args:
            number (int): Value to add.
        """
        self.data[number] += 1
        
    def build_stats(self) -> Stats:
        """Function to send all data to be processed all the data to create the stats.

        Returns:
            Stats: An object with all the processed data.
        """
        return Stats(self.data)