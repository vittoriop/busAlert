#!/usr/bin/env python

import urllib2
import re
from subprocess import call
import datetime
# import time
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('/home/vittorio/Code/myRepo/Python/busAlert/busAlert.cfg')

stops = config.get('Data', 'Stops')
stops = eval(stops)
bus = config.get('Data', 'Buses')
bus = eval(bus)

timeToStop = {'2571': 12, '7117': 5, '1177': 10}
timeToGym = {'#71C': 33, '#67': 20, '#69': 20, '#61A': 30, '#71D': 25}

triple = []     # (stop/bus line/time)

for s in stops:
    busLines = []
    times = []
    url = 'http://truetime.portauthority.org/bustime/wireless/html/eta.jsp?route=---&direction=---&displaydirection=---&stop=---&id='
    response = urllib2.urlopen(url+s)
    html = response.read()
    if 'No arrival times available.' in html:
        print 'No bus arriving at '+s
    else:
        lines = html.split('\n')
        for l in lines:
            r = re.search("#[0-9]{2}[A-Z]?&nbsp", l)
            if r:
                busLines.append(r.group(0)[0:-5])
            r = re.search("[0-9]+&nbsp;MIN", l)
            if r:
                times.append(int(r.group(0)[0:-9]))
    for b, t in zip(busLines, times):
        triple.append((s, b, t))


# print busLines
# print times

triple.sort(key=lambda tup: tup[2])
output = ''
t = datetime.datetime.now()
for elem in triple:
    if any([x in elem for x in bus]):
        extraTime = elem[2] + timeToGym[elem[1]]
        output += "%s stopping by in %d'. <i>ETA: %s</i>\n" % (elem[1], elem[2],
                                                        format(t+datetime.timedelta(minutes=extraTime), '%H:%M'))
# print output
if output == '':
    output = "No bus coming anytime soon!"

# f = open('/home/vittorio/Desktop/cron.txt', 'a')
# f.write(str(time.time()) + '\t' + output)
call(['notify-send', '-i', '/home/vittorio/Code/portauthority/bus.png',
      "Bus Alert", output])
