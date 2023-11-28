from exceptions.exceptions import check_integers

class Stats:
    def __init__(self, data):
        for number in range(1,len(data)):
            data[number]+=data[number-1]
        self.data = data
            
    @check_integers
    def less(self, number):
        return self.data[number-1]
            
    @check_integers
    def greater(self, number):
        return self.data[-1] - self.data[number]
            
    @check_integers
    def between(self, begin, finish):
        dif = self.data[begin-1] if begin != 0 else 0
        return self.data[finish] - dif