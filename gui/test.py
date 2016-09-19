import sys
from PyQt4.QtGui import QApplication, QDialog
from config import Ui_Dialog  # here you need to correct the names
import ConfigParser


app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)
config = ConfigParser.RawConfigParser()
config.read('../busAlert.cfg')
print config
if config is not []:
    stops = config.get('Data', 'Stops')
    bus = config.get('Data', 'Buses')
    ui.BusText.append(stops)

window.show()
sys.exit(app.exec_())
