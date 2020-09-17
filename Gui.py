from AutoGUI import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from comp import Pendulum
from style import STYLESHEET
class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Compound Pendulum")
        self.tabs = QTabWidget()
        pendUi = PendulumInterface()
        about = About()
        diagram = SystemDiagram()
        self.tabs.addTab(about, "About")
        self.tabs.addTab(pendUi, "Pendulum")
        self.tabs.addTab(diagram, "System Diagram")
        self.setStyleSheet(STYLESHEET)
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(self.tabs)

class About(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()
        my_text_edit = QTextEdit()
        my_text_edit.setReadOnly(True)
        my_text_edit.textCursor().insertHtml('''  <div class="resume-item pb-0">
            <h4>Vera Worri</h4>
            <p><em>Innovative and persistent problem solver who is customer focused.</em></p>
            <p>
            <ul>
              <li>Reston, VA</li>
              <li>(904) 728-1472</li>
              <li>vworri@gmail.com</li>
            </ul>
            </p>
              </div>
          <h3 class="resume-title">Education</h3>
          <div class="resume-item">
            <h4>Bachelors of Science: ; Physics</h4>
            <h5>2010 - 2014</h5>
            <p><em>Eckerd College, St. Petersburg, FL</em></p>
            <p>
            Solving skills with mathemetics and scientific reasoning.
            </p>
          </div>
        </div>''')
        layout.addWidget(my_text_edit)
        self.setLayout(layout)

class SystemDiagram(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Diagram")
        my_text_edit = QTextEdit()
        my_text_edit.setReadOnly(True)
        my_text_edit.textCursor().insertHtml("""
        <h1>Compound Pendulum</h1>
        <p>
        The system is programmed as drawn adjacent. There is a pendulum with a metal disk on the end that is free to swing back and forth.
        </p>
        <p>
        There is a magnet at the bottom of the swing who's field's strength is programmable. In addition, a driving or dampening force can be added.
        </p>
        <p>
        Parameters are initialized for chaos!!!!!
        </p>
        """)
        label = QLabel(self)
        pixmap = QPixmap('compoundpendulum.jpg')
        label.setPixmap(pixmap)
        scroll = QScrollArea()
        scroll.setWidget(label)
        scroll.setWidgetResizable(True)
        layout = QHBoxLayout(self)
        
        layout.addWidget(scroll)
        layout.addWidget(my_text_edit)
        self.setLayout(layout)
        
class PendulumInterface(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(PendulumInterface, self).__init__(parent)
        self.pendulum = Pendulum()
        self.setWindowTitle("Compound Pendulum Simulator")
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
        QDialog.accept(self)

    def reject(self,):
        global done
        done = True
        QDialog.reject(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    status = app.exec_()
    sys.exit(status)