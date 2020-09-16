from AutoGUI import Ui_Dialog
from PyQt5 import QtWidgets
from comp import Pendulum

class UserInterface(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(UserInterface, self).__init__(parent)
        self.pendulum = Pendulum()
        self.setupUi(self)
        self.md.setValue(self.pendulum.md)
        self.Dr.setValue(self.pendulum.Dr)
        self.Da.setValue(self.pendulum.Da)
        self.mr.setValue(self.pendulum.mr)
        self.l.setValue(self.pendulum.l)
        self.Res.setValue(self.pendulum.Res)
        self.r.setValue(self.pendulum.R)
        self.MagField.setValue(self.pendulum.B)
        self.t.setValue(self.pendulum.p)
        self.omegaD.setValue(self.pendulum.omegaD)

    def main(self):
        self.show()

    def accept(self):
        self.pendulum.md = self.md.value()
        self.pendulum.Dr = self.Dr.value()
        self.pendulum.Da = self.Da.value()
        self.pendulum.mr = self.mr.value()
        self.pendulum.l = self.l.value()
        self.pendulum.Res = self.Res.value()
        self.pendulum.R = self.r.value()
        self.pendulum.B = self.MagField.value()
        self.pendulum.p = self.t.value()
        self.pendulum.omegaD = self.omegaD.value()
        self.pendulum.calculate()
        QtWidgets.QDialog.accept(self)

    def reject(self,):
        global done
        done = True
        QtWidgets.QDialog.reject(self)

