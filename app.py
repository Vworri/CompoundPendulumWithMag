# Vera Worri
# driven and dampened compound pendulum with bar magnet at theta= 90 degrees
#######################################################################################################################
#imported packages

from Gui import MainWindow
from PyQt5 import QtWidgets, QtGui
import sys


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.setWindowIcon(QtGui.QIcon('default.ico'))
    window.setWindowIcon(QtGui.QIcon('default.ico'))
    window.show()
    status = app.exec_()
    sys.exit(status)





