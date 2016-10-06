import sys
from PyQt4.QtGui import QApplication, QDialog
from loadConfig import Ui_Dialog  # here you need to correct the names
import ConfigParser
import os
import subprocess


def makeCrontabLine(dayStart, dayEnd, timeStart, timeEnd, freq):

    line = ''
    line += "*/%s " % freq
    line += "%d-%d * * " % (int(timeStart[0:2]), int(timeEnd[0:2]))
    line += '%s-%s ' % (dayStart, dayEnd)

    return line


class mainWindow(QDialog):

    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.dayEnd.setCurrentIndex(6)
        self.ui.timeStart.addItems(['%02d:00' % x for x in range(0, 24)])
        self.ui.timeEnd.addItems(['%02d:00' % x for x in range(0, 24)])
        self.ui.timeEnd.setCurrentIndex(23)
        self.ui.pushButton.clicked.connect(self.on_ok)
        self.ui.freq.addItems([str(x) for x in range(1, 61)])

    def on_ok(self):
        # read data about bus stops and bus lines
        newStop = str(self.ui.StopText.text()).split(',')
        stopToConfig = str([elem.strip() for elem in newStop])
        newBus = str(self.ui.BusText.text()).split(',')
        busToConfig = str([elem.strip() for elem in newBus])

        # write on config file
        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        configFile = open(path + "/busAlert.cfg", "w")
        configFile.write("[Data]\n\n")
        configFile.write("Buses = " + busToConfig + "\n")
        configFile.write("Stops = " + stopToConfig + "\n")
        configFile.close()

        # read data to set the cron job
        dStart = str(self.ui.dayStart.currentText())
        dEnd = str(self.ui.dayEnd.currentText())
        tStart = str(self.ui.timeStart.currentText())
        tEnd = str(self.ui.timeEnd.currentText())
        freq = str(self.ui.freq.currentText())

        # write to cron
        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        toCron = makeCrontabLine(dStart, dEnd, tStart, tEnd, freq)
        toCron += path + "/loadenv.sh   # automatically added by busAlert\n"
        currentCron = subprocess.check_output(['crontab', '-l'])
        # TODO: parse cron to replace(?) older setting
        #       delete tmp file
        tmp = open('tmpCron', 'w')
        tmp.write(currentCron + toCron)
        tmp.close()
        subprocess.call(['crontab', 'tmpCron'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWindow()
    config = ConfigParser.RawConfigParser()
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    config.read(path + '/busAlert.cfg')
    try:
        stops = config.get('Data', 'Stops')
        stops = eval(stops)
        window.ui.StopText.setText(', '.join(stops))
    except:
        pass
    try:
        bus = config.get('Data', 'Buses')
        bus = eval(bus)
        window.ui.BusText.setText(', '.join(bus))
    except:
        pass

    window.show()
    sys.exit(app.exec_())
