import scipy.integrate as integrate
from pylab import *


class Pendulum(object):
    def __init__(self):
        self.p = 0.01
        self.Dr = 0  # sinusoidal driving coefficient
        self.Da = 0  #damping coefficient
        self.mr = 0.5  #mass of pendulum arm
        self.md = 0.05  #mass of disk
        self.l = 1  #length from disk to pivot
        self.R = 0.025  # radius of the disk
        self.B = 0.005
        self.Res = 1
        self.g = 9.8  #gravity
        self.C = 2 * self.R * self.R * math.pi
        self.t = arange(0, 100, self.p)  # time step
        self.omegaD = ((1/2*pi)*((1/2)*self.mr + self.md)*self.g*self.l/(((1/3)*self.mr + self.md)*self.l**2))  #driving frequency reminder: two different frequencies
        self.A = math.pi * self.R * self.R  # area of disc
        self.sigma = 0.5  #gaussian coefficient = gaussian variance
        self.oms = (self.Res * 10 ** -8) * (self.C / self.A)  #resistance of disc metal (copper)
        self.mu = 2.6 * self.sigma  # gaussian shift = expected value
 ########################################################################################################################

########################################################################################################################

#System function
    def system_function(self,r, t):
        theta = r[0]
        self.omega = r[1]
        ftheta = self.omega
        fomega = self.AngularAcceleration(theta) - self.Damped() +self.Driving(t) - self.Balpha(theta)
        return [ftheta, fomega]
    #######################################################################################################################
    #Moment of inertia
    def Moment(self):
        return ((1/3)*self.mr*self.l**2) + (self.md*self.l**2)+((1/2)*self.md*self.R**2)

    #######################################################################################################################
    #gaussian
    def GaussianPositive(self,theta):
        return (1 / self.sigma * (2 * math.pi) ** 0.5) * math.e ** (-0.5 * ((theta - self.mu) / self.sigma) ** 2)


    def GaussianNegative(self, theta):
        return -(1 / self.sigma * (2 * math.pi) ** 0.5) * math.e ** (-0.5 * ((self.mu + theta) / self.sigma) ** 2)


    def gaussian(self,theta):
        if theta < 0:
            return self.GaussianPositive(theta)
        else:
            return self.GaussianNegative(theta)


    #######################################################################################################################
    #induced current
    def induced_current(self,theta, omega):
        return -(self.B * 0.5 * self.R ** 2 * self.omega) / self.oms


    ########################################################################################################################
    # magnetic dampening/driving: angular acceleration due to mag field
    def Balpha(self,theta):
        return (self.induced_current(theta, self.omega) * self.B * self.A * math.sin(theta)) / (.5 *self.md * self.R ** 2) * self.gaussian(theta)


    ########################################################################################################################
    #damping term
    def Damped(self):
        return self.Da * (self.omega)


    ########################################################################################################################
    #driving term
    def Driving(self, t):
        return self.Dr * math.cos(self.omegaD * t)
    ########################################################################################################################
    #compound pendulum intrinsic angular acceleration
    def AngularAcceleration(self,theta):
        return (-.5 * (self.mr + self.md)) * self.g * self.l * math.sin(theta) / (((1 / 3) * self.mr + self.md) * self.l ** 2 + 0.5 * self.md * self.R * self.R)
    ########################################################################################################################
    #momentum
    def Momentum(self,theta, omega):
        return self.Moment()*sin(theta)*omega
    ########################################################################################################################

    def calculate(self):
        f_int = [3, 0.0]
        kinematics = integrate.odeint(self.system_function, f_int, self.t)
        position = kinematics[:, 0]
        AngularVelocity = kinematics[:, 1]
        figure(1)
        suptitle('Time vs Angular Velocity')
        plot(self.t,AngularVelocity)
        figure(2)
        suptitle('Position vs Momentum')
        plot(position, self.Momentum(position ,AngularVelocity))
    #######################################################################################################################
        #Create graphs in polar
        figure(3)
        plt.subplot(211, projection='polar')
        plt.title("A line plot of the pendulum moving on the polar axis,\n theta=Angular Velocity versus r=Time")
        plot(AngularVelocity, self.t)
        plt.subplot(212, projection='polar',label="Angular Velocity vs Position")
        plt.title("A line plot of the pendulum moving on the polar axis,\n Angular Velocity versus Position\n\n\n")
        plot(AngularVelocity, position)
        plt.tight_layout()

        show()
if __name__ == '__main__':
    s = Pendulum()
    s.calculate()