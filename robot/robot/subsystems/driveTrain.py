# -*- coding: utf-8 -*-
import wpilib

from wpilib.command.subsystem import Subsystem
import wpilib.drive.differentialdrive as dd

import robot as robotPackage

class DriveTrainSub(Subsystem):
    '''
    This is the subsystem to controller the robots wheels.
    '''
    
    def __init__(self, robot):
        '''Initilizes the subsystem, gets the motors, 
        creates the drivetrain mixer
        '''
        super().__init__("DriveTrainSub")
        #self.robot = robotPackage.MyRobot.getRobot()
        self.robot = robot
        self.driveMotors = self.robot.driveMotors
        self.driveTrain = dd.DifferentialDrive(**self.driveMotors)
        
    def setTankDrive(self, leftSide, rightSide):
        self.driveTrain.tankDrive(leftSide, rightSide)
        
    def setArcadeDrive(self, speed, rot):
        self.driveTrain.arcadeDrive(speed, rot)
