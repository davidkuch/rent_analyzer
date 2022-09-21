from unicodedata import name
from CsvDataSource import CsvDataSource
from datetime import datetime
from Researcher import Researcher

def cli_server(): # TODO: optionally accept command line arguments for filename and date
    '''takes filename and date, prints research results'''

    filename = input("please enter csv filename: ")

    data = CsvDataSource(filename).getData()
    researcher = Researcher(data)

    print("total indefinitely reserved at some time: ", researcher.CountReservedIndefinitely())
    print("toal number of officies: ", researcher.CountOfficies())


    print("------------")


    while(True):
        raw_input = input("enter date(YYYY-MM): ")
        month = datetime.strptime(raw_input, '%Y-%m').date()

        print("date: {}-{}".format(month.year, month.month))
        print("count reserved for month:", researcher.CountReservedForMonth(month))
        print("capacity unreserved for month:", researcher.CapacityUnreservedForMonth(month))
        print("profit for month: {0:.2f}".format(researcher.ProfitForMonth(month)))
        print("average profit from office in the month: {0:.2f}".format(researcher.AverageProfitForReservedOffice(month)))

        print("------------")


if __name__ == '__main__':
    cli_server()