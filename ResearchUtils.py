from datetime import datetime



def ReservedInMonth(office: dict, month : datetime) ->bool:
    '''true if office is reserved in given month even one day'''
    return office['Start Day'] <= month <= office['End Day']


def ReservedIndefinitely(office: dict) -> bool:
    '''true if office is reserved indefinitely from any date''' 
    return office['End Day'] == datetime.max.date()


def ProfitForMonth(office: dict, month : datetime) ->int:
    '''check before if the office is reserved in the month!''' 
    return office["Monthly Price"] * (daysReservedInMonth(office, month) / 30)

    
def daysReservedInMonth(office: dict, month : datetime) -> int:
    '''returnes number of days the office is reserved for given month'''
    start = -1

    if office['Start Day'].month < month.month:
         start = 1
    if office['Start Day'].month == month.month:
        start = office['Start Day'].day
        
    end = -1

    if office['End Day'].month > month.month:
        end = 30
    if office['End Day'].month == month.month:
        end = office['End Day'].day

    if start == -1 or end == -1:
        return 0

    if start == end:
        return start

    return end - start

    