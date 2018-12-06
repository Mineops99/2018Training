#!/usr/bin/env python3
'''
    This is a demo program showing how to use Mecanum control with the
    RobotDrive class.
'''

import wpilib

import commandbased
import ctre

import subsystems.driveTrain

#main robot

class MyRobot(commandbased.CommandBasedRobot):
    
    def robotInit(self):
        MyRobot.getRobot = lambda x=0:self
        self.driveMotors = {}
        self.driveMotors['leftMotor'] = ctre.WPI_TalonSRX(0)
        self.driveMotors['rightMotor'] = ctre.WPI_TalonSRX(1)

        self.dtSub = subsystems.driveTrain.DriveTrainSub(self)
        self.driveController = wpilib.XboxController(0)

    def teleopInit(self):
        print("Test Mode")
        dc = self.driveController
        while self.isOperatorControl():
            leftSide = dc.getRawAxis(0)
            rightSide = dc.getRawAxis(1)
            self.dtSub.setTankDrive(leftSide,rightSide)
            
        print("Test Done")
            





#code to help run the robot

#import sys       
def exit(retval):
    pass
#    sys.exit(retval)

if __name__ == '__main__':
    try:
        print(wpilib._impl.main.exit)
    except:
        wpilib._impl.main.exit = exit
    wpilib.run(MyRobot,physics_enabled=True)