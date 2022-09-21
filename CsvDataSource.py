import csv 
from datetime import datetime
import copy

class CsvDataSource:
    def __init__(self,filename):
        '''creates a data object( list of dicts) from a csv file'''
        file = open(filename)
        obj = csv.DictReader(file)
        obj = self.clean_csv(obj)
        self.obj = self.parse_csv(obj)
        
        file.close()

    
    def getData(self):
        '''returnes data object ready to research, as list of dicts'''
        return self.obj
    
    def clean_csv(self,obj):
        '''cleans the csv dict object'''

        # maybe more cleaning would be added in later version
        return self.removeEmptyLines(obj)


    def removeEmptyLines(self, obj):
        ''' removes empty lines '''
        ret = [line for line in obj if line["Capacity"].isdigit() == True]
        return ret


    def parse_csv(self, clean_obj):
        '''parses the date and int-string fields to date objects and ints'''
        ret = []
        to_attach = {}

        #TODO: this assumes that names are exactly as in the test input file.
        #      must make it work with some variation as well
        for line in clean_obj:
            to_attach["Capacity"] = int(line["Capacity"])
            to_attach["Monthly Price"] = int(line[" Monthly Price"])
            to_attach["Start Day"] = datetime.strptime(line[" Start Day"].strip(), '%Y-%m-%d').date()
            if (line[" End Day"] != ''):
                to_attach["End Day"] = datetime.strptime(line[" End Day"].strip(), '%Y-%m-%d').date()
            else:
                to_attach["End Day"] = datetime.max.date() # rented indefinitely
            

            ret.append(copy.deepcopy(to_attach))

        return ret
