from django import forms
import datetime
import arrow
from dateutil import parser

class bookingForm(forms.Form):
    dateStart = datetime.datetime.now().date()
    #dateStart = datetime.datetime.strptime(str(dateStart), '%Y-%d-%m').strftime("%d/%m-%Y")
    #datetime.datetime.strptime("21/12/2008", "%d/%m/%Y").strftime("%Y-%m-%d")
    print (datetime.date.today().strftime("%m"))
    print (datetime.date.today().strftime("%d"))
    print (datetime.date.today().strftime("%Y"))
    dateStart = datetime.date.today().strftime("%d-%m-%Y")
    dateStart = parser.parse(dateStart)
    print "dateStart:",dateStart
    dateArr = []
    for i in range(100):
        dateStart += datetime.timedelta(days=1)
        #print(dateStart)
        dateStart2 = dateStart.strftime("%d-%m-%Y")
        dateArr.append((str(dateStart2), str(dateStart2),))
    MONTH_CHOICES = [(i, i,) for i in xrange(1, 13)]
    #print "dateArr Type",type(dateArr)
    #print "dateArr:",dateArr
    #print "Month Choices Type:",type(MONTH_CHOICES)
    #print "month c:",MONTH_CHOICES
    start_date = forms.ChoiceField(label="Start Date", choices=dateArr)
    end_date = forms.ChoiceField(label="End Date", choices=dateArr)
