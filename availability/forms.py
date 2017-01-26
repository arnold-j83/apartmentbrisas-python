from django import forms
import datetime
import arrow
from dateutil import parser
import json
import urllib2

class bookingForm(forms.Form):
    url = 'https://www.googleapis.com/calendar/v3/calendars/catkin.order@gmail.com/events?maxResults=15&key=AIzaSyDy4L8f1AMz49DEbNYrsJkn5Jr18lJRDhg'
    data = json.load(urllib2.urlopen(url))
    dataitems = data['items']

    dateArr2 = []
    for itemss in dataitems:
        itemend = itemss['end']['date']
        itemstart = itemss['start']['date']
        itemend = str(itemend)
        itemstart = str(itemstart)
        itemstart = parser.parse(itemstart)
        itemend = parser.parse(itemend)
        daysdif = abs((itemstart - itemend).days)
        itemstart2 = itemstart.strftime("%d-%m-%Y")
        dateArr2.append(itemstart2)

        for i in range(daysdif - 1):
            itemstart += datetime.timedelta(days=1)
            itemstart2 = itemstart.strftime("%d-%m-%Y")
            print "itmst2:",itemstart2
            dateArr2.append(str(itemstart2))


    print "dateArr:",dateArr2

    dateStart = datetime.datetime.now().date()

    dateStart = datetime.date.today().strftime("%d-%m-%Y")
    dateStart = parser.parse(dateStart)
    dateArr = []
    dateArrSimple = []
    dateArrSimple2 = []
    for i in range(100):
        dateStart += datetime.timedelta(days=1)
        dateStart2 = dateStart
        dateStart2 = dateStart2.strftime("%d-%m-%Y")
        #dateArr.append((str(dateStart2), str(dateStart2),))
        dateArrSimple.append(str(dateStart2))
        dateArrSimple2.append(str(dateStart2))
    dateStart2 = datetime.date.today().strftime("%d-%m-%Y")
    dateStart2 = parser.parse(dateStart2)
    dateArrExc = []
    #print "dateArrSimpleBefore:", dateArrSimple2
    for ii in dateArrSimple:
        for jj in dateArr2:
            if str(ii) == str(jj):
                print "datetoexclude2:",str(ii)
                dateArrSimple2.remove(ii)

    #print "dateArrSimpleAfter:",dateArrSimple2

    for i in dateArrSimple2:
        dateArr.append((str(i), str(i),))

    #dateArrSimple.remove('27-01-2017')
    #print "dateArrSimple:", dateArrSimple
    #print "dateArrN:", dateArr
    MONTH_CHOICES = [(i, i,) for i in xrange(1, 13)]
    #print "dateArr Type",type(dateArr)
    #print "dateArr:",dateArr
    #print "Month Choices Type:",type(MONTH_CHOICES)
    #print "month c:",MONTH_CHOICES
    start_date = forms.ChoiceField(label="Start Date", choices=dateArr)
    end_date = forms.ChoiceField(label="End Date", choices=dateArr)
