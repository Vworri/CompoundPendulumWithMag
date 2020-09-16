# Vera Worri
# driven and dampened compound pendulum with bar magnet at theta= 90 degrees
#######################################################################################################################
#imported packages

from Gui import UserInterface
from PyQt5 import QtWidgets



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = UserInterface()
    window.main()
    status = app.exec_()
    sys.exit(status)





