import sys
from PyQt4.QtGui import QApplication, QDialog
from loadConfig import Ui_Dialog  # here you need to correct the names
import ConfigParser
import os


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
        newStop = str(self.ui.StopText.text()).split(',')
        stopToConfig = str([elem.strip() for elem in newStop])
        newBus = str(self.ui.BusText.text()).split(',')
        busToConfig = str([elem.strip() for elem in newBus])

        configFile = open("../busAlert.cfg", "w")
        configFile.write("[Data]\n\n")
        configFile.write("Buses = " + busToConfig + "\n")
        configFile.write("Stops = " + stopToConfig + "\n")

        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

        freq = "*/" + str(self.ui.freq.currentText())
        line = freq + " * * * * " + path + "/loadenv.sh"

        print line


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWindow()
    config = ConfigParser.RawConfigParser()
    config.read('../busAlert.cfg')
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
