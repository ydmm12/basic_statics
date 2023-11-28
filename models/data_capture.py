from models.stats import Stats
from exceptions.exceptions import check_integers

class DataCapture:
    data = [0] * 1000
    
    @check_integers
    def add(self, number):
        self.data[number] += 1
        
    def build_stats(self):
        return Stats(self.data)