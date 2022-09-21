from CsvDataSource import CsvDataSource
from datetime import datetime
from Researcher import Researcher


data = CsvDataSource("rent_data.csv").getData()
researcher = Researcher(data)


test_inputs = ['2013-01', '2013-06', '2014-03','2014-09','2015-07']
test_dates = [datetime.strptime(x, '%Y-%m').date() for x in test_inputs]


print("toal number of officies: ", researcher.CountOfficies())
print("total indefinitely reserved at some time: ", researcher.CountReservedIndefinitely())

print("------------")


for month in test_dates:
    print("date: {}-{}".format(month.year, month.month))
    print("count reserved for month:", researcher.CountReservedForMonth(month))
    print("capacity unreserved for month:", researcher.CapacityUnreservedForMonth(month))
    print("profit for month: {0:.2f}".format(researcher.ProfitForMonth(month)))
    print("average profit from office in the month: {0:.2f}".format(researcher.AverageProfitForReservedOffice(month)))
    print("------------")
