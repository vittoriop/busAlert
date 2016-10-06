#!/usr/bin/env python

import urllib2
import re
from subprocess import call
import datetime
import ConfigParser
import os


def check(smtg='None'):
    config = ConfigParser.RawConfigParser()
    path = os.path.dirname(os.path.realpath(__file__))
    config.read(path+'/busAlert.cfg')

    stops = config.get('Data', 'Stops')
    stops = eval(stops)
    bus = config.get('Data', 'Buses')
    bus = eval(bus)

    triple = []     # (stop/bus line/time)

    for s in stops:
        busLines = []
        times = []
        url = 'http://truetime.portauthority.org/bustime/wireless/html/eta.jsp?route=---&direction=---&displaydirection=---&stop=---&id='   #noqa
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

    triple.sort(key=lambda tup: tup[2])
    output = ''
    t = datetime.datetime.now()
    for elem in triple:
        if any([x in elem for x in bus]):
            output += "%s stopping by in %d'\n" % (elem[1], elem[2])
    if output == '':
        output = "No bus coming anytime soon!"

    call(['notify-send', '-i', path+'/bus.png',
          "Bus Alert", output])


if __name__ == "__main__":
    check()
