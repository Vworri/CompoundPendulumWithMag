# Vera Worri
# driven and dampened compound pendulum with bar magnet at theta= 90 degrees
#######################################################################################################################
#imported packages
import scipy.integrate as integrate
from pylab import *
from CompoundPendulumGUI import Ui_Dialog
from PyQt4 import QtGui
import sys
########################################################################################################################
#Variables
p = 0.01
Dr = 0  # sinusoidal driving coefficient
Da = 0  #damping coefficient
mr = 0.5  #mass of pendulum arm
md = 0.05  #mass of disk
l = 1  #length from disk to pivot
R = 0.025  # radius of the disk
B = 0.005
Res = 1
g = 9.8  #gravity
C = 2 * R * R * math.pi
t = arange(0, 100, p)  # time step
omegaD = ((1/2*pi)*((1/2)*mr + md)*g*l/(((1/3)*mr + md)*l**2))  #driving frequency reminder: two different frequencies
A = math.pi * R * R  # area of disc
sigma = 0.5  #gaussian coefficient = gaussian variance
oms = (Res * 10 ** -8) * (C / A)  #resistance of disc metal (copper)
mu = 2.6 * sigma  # gaussian shift = expected value
########################################################################################################################

########################################################################################################################
#System function
def f(r, t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = AngularAcceleration(theta) - Damped(omega) + Driving(omega, t) - Balpha(theta, omega)
    return [ftheta, fomega]
#######################################################################################################################
#Moment of inertia
def Moment():
    return ((1/3)*mr*l**2) + (md*l**2)+((1/2)*md*R**2)

#######################################################################################################################
#gaussian
def GaussianPositive(theta):
    return (1 / sigma * (2 * math.pi) ** 0.5) * math.e ** (-0.5 * ((theta - mu) / sigma) ** 2)


def GaussianNegative(theta):
    return -(1 / sigma * (2 * math.pi) ** 0.5) * math.e ** (-0.5 * ((mu + theta) / sigma) ** 2)


def G(theta):
    if theta < 0:
        return GaussianPositive(theta)
    else:
        return GaussianNegative(theta)


#######################################################################################################################
#induced current
def I(theta, omega):
    return -(B * 0.5 * R ** 2 * omega) / oms


########################################################################################################################
# magnetic dampening/driving: angular acceleration due to mag field
def Balpha(theta, omega):
    return (I(theta, omega) * B * A * math.sin(theta)) / (.5 * md * R ** 2) * G(theta)


########################################################################################################################
#damping term
def Damped(omega):
    return Da * (omega)


########################################################################################################################
#drivng term
def Driving(omega, t):
    return Dr * math.cos(omegaD * t)
########################################################################################################################
#compound pendulum intrinsic angular acceleration
def AngularAcceleration(theta):
    return (-.5 * (mr + md)) * g * l * math.sin(theta) / (((1 / 3) * mr + md) * l ** 2 + 0.5 * md * R * R)
########################################################################################################################
#momentum
def Momentum(theta, omega):
    return Moment()*sin(theta)*omega
########################################################################################################################
def calculate():
    f_int = [3, 0.0]
    kinematics = integrate.odeint(f, f_int, t)
    position = kinematics[:, 0]
    AngularVelocity = kinematics[:, 1]
    figure(1)
    suptitle('Time vs Angular Velocity')
    plot(t,AngularVelocity)
    figure(2)
    suptitle('Position vs Momentum')
    plot(position, Momentum(position ,AngularVelocity))
#######################################################################################################################
    #Create graphs in polar
    figure(3)
    plt.subplot(211, projection='polar')
    plt.title("A line plot of the pendulum moving on the polar axis,\n theta=Angular Velocity versus r=Time")
    plot(AngularVelocity, t)
    plt.subplot(212, projection='polar',label="Angular Velocity vs Position")
    plt.title("A line plot of the pendulum moving on the polar axis,\n Angular Velocity versus Position\n\n\n")
    plot(AngularVelocity, position)
    plt.tight_layout()

    show()



#######################################################################################################################
class UserInterface(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(UserInterface, self).__init__(parent)
        self.setupUi(self)
        self.md.setValue(md)
        self.Dr.setValue(Dr)
        self.Da.setValue(Da)
        self.mr.setValue(mr)
        self.l.setValue(l)
        self.Res.setValue(Res)
        self.r.setValue(R)
        self.MagField.setValue(B)
        self.t.setValue(p)
        self.omegaD.setValue(omegaD)

    def main(self):
        self.show()

    def accept(self):
        global B, md,Dr,Da,mr,l,Res,R,p,omegaD
        md = self.md.value()
        Dr = self.Dr.value()
        Da = self.Da.value()
        mr = self.mr.value()
        l = self.l.value()
        Res = self.Res.value()
        R = self.r.value()
        B = self.MagField.value()
        p = self.t.value()
        omegaD = self.omegaD.value()
        calculate()
        QtGui.QDialog.accept(self)

    def reject(self,):
        global done
        done = True
        QtGui.QDialog.reject(self)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = UserInterface()
    done = False
    while not done:
        window.main()
        status = app.exec_()
    sys.exit(status)





