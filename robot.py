#!/usr/bin/env python3 # <---- This runs the code
'''
Super Sketch Experimental Drive that no team should attempt to recreate
'''


import wpilib
import wpilib.buttons
from wpilib.drive import DifferentialDrive

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):

        self.LeftMec = wpilib.Talon(0)
        self.RightMec = wpilib.Talon(1)
        self.robotDrive = wpilib.RobotDrive(self.LeftMec, self.RightMec)
        self.pg = wpilib.Talon(2)
        self.xboxController = wpilib.XboxController(0)# <-- This is for using Xbox controllers

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
#        self.LeftMec.set(self.xboxController.getY(0))
 #       self.RightMec.set(-1 * self.xboxController.getY(0))
        self.pg.set(0.30 * self.xboxController.getX(1))
        self.robotDrive.arcadeDrive(self.xboxController.getY(0) / 2,self.xboxController.getX(0) / 2)
if __name__ == "__main__":
    wpilib.run(MyRobot)