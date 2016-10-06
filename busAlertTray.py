from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from subprocess import call
from busAlert import check
import os

APPINDICATOR_ID = 'myappindicator'

def build_menu():
    menu = gtk.Menu()
    item_quit = gtk.MenuItem('Quit')
    item_check = gtk.MenuItem('Check Now!')
    item_config = gtk.MenuItem('Config')
    item_quit.connect('activate', quit)
    item_check.connect('activate', check)
    item_config.connect('activate', config)
    menu.append(item_check)
    menu.append(item_config)
    menu.append(item_quit)
    menu.show_all()
    return menu


def config(source):
    call(['python', './gui/configUi.py'])


def quit(source):
    gtk.main_quit()

def main():
    # indicator = appindicator.Indicator.new(APPINDICATOR_ID, 'whatever',
    #                                        appindicator.IndicatorCategory.SYSTEM_SERVICES)

    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('bus.png'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()

if __name__ == "__main__":
    main()
