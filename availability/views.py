from django.shortcuts import render
import json
import urllib2
from dateutil import parser
#from datetime import datetime
import datetime
import arrow
from .forms import bookingForm
def get_index(request):

    url = 'https://www.googleapis.com/calendar/v3/calendars/catkin.order@gmail.com/events?maxResults=15&key=AIzaSyDy4L8f1AMz49DEbNYrsJkn5Jr18lJRDhg'
    data = json.load(urllib2.urlopen(url))
    dataitems = data['items']
    dataitems2 = json.dumps(dataitems)
    #print dataitems
    #print dataitems2
    dateArr = []
    for itemss in dataitems:
        itemend = itemss['end']['date']
        itemstart = itemss['start']['date']
        itemend = str(itemend)
        itemstart = str(itemstart)
        #print "item start:", itemstart
        itemstart = parser.parse(itemstart)
        #print "itemstart type:", type(itemstart)
        itemend = parser.parse(itemend)
        #print "item end:", itemend
        #print "itemend type:", type(itemend)
        daysdif = abs((itemstart - itemend).days)
        #print "daysdiff:",daysdif
        dateArr.append(itemstart)

        for i in range(daysdif - 1):
            itemstart += datetime.timedelta(days=1)
            #print(itemstart)
            dateArr.append(itemstart)
        #print dateArr

        #dateStart = datetime.datetime.now().date()
        #dateArr2 = []
        #for i in range(10):
        #    dateStart += datetime.timedelta(days=1)
            #print(dateStart)
        #    dateArr2.append(dateStart)
        #print dateArr2

    if request.method == 'POST':
        form = bookingForm(request.POST)
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        print "start date",start_date
        print "end date", end_date
        start_date_parsed = parser.parse(start_date)
        end_date_parsed = parser.parse(end_date)
        daysDiff2 = abs((start_date_parsed - end_date_parsed).days)
        print daysDiff2
        dateArr3 = []
        dateArr3.append(start_date_parsed)
        for i in range(daysDiff2):
            start_date_parsed += datetime.timedelta(days=1)
            #print(itemstart)
            dateArr3.append(start_date_parsed)
        print "dateArr:",dateArr
        print "dateArr3",dateArr3

        dateArr4 = []

        for ii in dateArr:
            #print ii
            for jj in dateArr3:
                if ii == jj:
                    print ii
                    dateArr4.append(ii)
        print "dateArr4:",dateArr4


    else:
        form = bookingForm()

    args = {'form': form}
    return render(request, 'availability.html', args)

