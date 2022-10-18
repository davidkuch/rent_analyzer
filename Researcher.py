from datetime import datetime
from itertools import count
from sqlite3 import Row
from ResearchUtils import *


class Researcher:
    '''object for aggregate queries on the data - takes the data object that CsvDataSource produces'''
    def __init__(self, data):
        self.data = data


    def CountReservedForMonth(self, month : datetime) -> int:
        '''returnes number of reserved offices in given month'''
        count = 0

        for record in self.data:
            if ReservedInMonth(record, month):
                count += 1

        return count

    
    def CapacityUnreservedForMonth(self, month: datetime) -> int:
        '''returnes the capacity if the unreserved offices for given month'''
        capacity  = 0

        for record in self.data:
            if ReservedInMonth(record, month) == False:
                capacity += record['Capacity']

        return capacity

    
    def ProfitForMonth(self, month: datetime) -> int:
        '''returnes the total profit from all offices for given month'''
        profit = 0

        for record in self.data:
            if ReservedInMonth(record, month):
                profit += ProfitForMonth(record, month)

        return profit


    def CountReservedIndefinitely(self) -> int:
        '''returnes the total number of offices that are reserved indefinitely from some date'''
        count = 0

        for record in self.data:
            if ReservedIndefinitely(record):
                count += 1

        return count


    def CountOfficies(self):
        '''returnes total number of all officies in the data'''
        return  len(self.data)


    def AverageProfitForReservedOffice(self, month : datetime) -> int:
        '''returnes average profit from the reserved officies of given month'''
        if self.CountReservedForMonth(month) == 0:
            return 0
            
        return self.ProfitForMonth(month) / self.CountReservedForMonth(month)