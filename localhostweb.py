import os
import httplib2
import json

httpServer = httplib2.Http()
urlTurnOn = "http://192.168./toggle"

responseFromModule = httpServer.request(urlTurnOn, "GET")

class Move:
    def __init__(self, serverName, urlLink, return_json):
        self.server = serverName
        self.returnJsonServerName = return_json
        self.url = urlLink
        self.headers = {"Content-Type":"application/json; charset=UTF-8"}
        self.jsonList = {
            "bottomServoAction":"ActionHere",
            "firstArmPistonAction":"ActionHere",
            "secondArmPistonAction":"ActionHere",
            "thirdArmServoPullBackString":"ActionHere",
            "fourthArmPistonAction":"ActionHere",
            "gripperArmAction":"ActionHere"
                         }

    def moveBase(self, commandName):
        if commandName == "BASE_MOVE_LEFT":
            pass
            print("BASE_MOVE_LEFT Action")
            # Change move value of bottomServoAction to MOVEBASELEFT
        if commandName == "BASE_MOVE_RIGHT":
            pass
            print("BASE_MOVE_RIGHT Action")
            # Change move value of bottomServoAction to MOVEBASELEFT
        else:
            print("Unknown command\nPossible commands:{}, {}".format("BASE_MOVE_LEFT", "BASE_MOVE_RIGHT"))

    def moveArm(self, command, command2=None, command3=None, angle=0,  angle2=0,  angle3=0,  angle4=0, pinNumber=9, pinNumber2=10, pinNumber3=11, pinNumber4=12):
        pass

    def specialCommands(self, command, angle=0):
        pass

    def sendDataArduino(self):
        pass

    def gripArm(self, command, maxAngle, minAngle):
        pass

    def returnSensorData(self):
        pass
