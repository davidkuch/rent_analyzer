from datetime import datetime


class ResearchUtils:
    def ReservedInMonth(office: dict, month : datetime) ->bool:
        '''true if office is reserved in given month even one day'''
        return office['Start Day'] <= month <= office['End Day']


    def ReservedIndefinitely(office: dict) -> bool:
        '''true if office is reserved indefinitely from any date''' 
        return office['End Day'] == datetime.max.date()


    def ProfitForMonth(office: dict) ->int:
        '''check before if the office is reserved in the month!''' 
        return office["Monthly Price"] * ((30 - office['Start Day'].day + 1) / 30)

    