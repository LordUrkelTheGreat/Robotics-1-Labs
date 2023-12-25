ColorSensor_X = None
ColorSensor_Y = None
ColorSensor_Z = None
R = None
G = None
B = None
MAX = None
Grab_X = None
Grab_Y = None
Grab_Z = None
Place_Y = None
RedCount = None
Place_X = None
GreenCount = None
BlueCount = None
PlacingInterval = None
Place_Z = None

"""描述该功能...
"""
def getcoler():
  global ColorSensor_X, ColorSensor_Y, ColorSensor_Z, R, G, B, MAX, Place_X, PlacingInterval, Place_Y, Place_Z, RedCount, GreenCount, BlueCount
  dType.SetPTPCmdEx(api, 0, ColorSensor_X,  ColorSensor_Y,  ColorSensor_Z, 0, 1)
  dType.dSleep(1000)
  R = dType.GetColorSensorEx(api, 0)
  G = dType.GetColorSensorEx(api, 1)
  B = dType.GetColorSensorEx(api, 2)
  MAX = max([R, G, B])
  if MAX == R:
    print('Red')
    dType.SetPTPCmdEx(api, 0, (Place_X + PlacingInterval),  Place_Y,  (Place_Z + RedCount), 0, 1)
    RedCount = RedCount + 25
  elif MAX == G:
    print('Green')
    dType.SetPTPCmdEx(api, 0, Place_X,  Place_Y,  (Place_Z + GreenCount), 0, 1)
    GreenCount = GreenCount + 25
  else:
    print('Blue')
    dType.SetPTPCmdEx(api, 0, (Place_X - PlacingInterval),  Place_Y,  (Place_Z + BlueCount), 0, 1)
    BlueCount = BlueCount + 25
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(1000)


print('[SETTING UP] Place Dobot Magician near by the motor of conveyor belt, make sure the conveyor belt is in front of the Dobot, the two sensor is close by the motor. ')
print('[HOME] Restore to home position at first launch, please wait 30 seconds after turnning on the Dobot.')
print('[SET HOME] Open the Teaching and Playback module, save one point, and right click to set the home position.')
print('[COLOR RECOGNIZING] After start the sorting blockly demo, Dobot Magician will move to the top of the color sensor and hold a while. Please adjust the position if it is not correct.')
print('[DIRECTION] Standing behind the Dobot Magician facing its front direction, X is front and back direction, Y is right and left direction.')
print('[COLOR SENSOR] Please connect the color sensor to GP4.')
print('[PHOTOELECTRIC SENSOR]Please connect the photoelectric sensor to GP2.')
Grab_X = 263
Grab_Y = 113
Grab_Z = 5
ColorSensor_X = 190
ColorSensor_Y = 110
ColorSensor_Z = 27
Place_X = 173
Place_Y = -150
Place_Z = -49
PlacingInterval = 40
dType.SetEndEffectorParamsEx(api, 59.7, 0, 0, 1)
RedCount = 0
BlueCount = 0
GreenCount = 0
dType.SetColorSensor(api, 1 ,1, 1)
dType.SetInfraredSensor(api, 1 ,2, 1)
dType.dSleep(1000)
dType.SetPTPJointParamsEx(api,400,400,400,400,400,400,400,400,1)
dType.SetPTPCommonParamsEx(api,90,90,1)
dType.SetPTPJumpParamsEx(api,50,100,1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, ColorSensor_X,  ColorSensor_Y,  ColorSensor_Z, current_pose[3], 1)
dType.SetEndEffectorSuctionCupEx(api, 0, 1)
while True:
  print('While Loops')
  if (dType.GetInfraredSensor(api, 2)[0]) == 1:
    print('Inside Loop')
    dType.SetEndEffectorSuctionCupEx(api, 1, 1)
    dType.SetPTPCmdEx(api, 0, Grab_X,  Grab_Y,  Grab_Z, 0, 1)
    getcoler()
    dType.SetPTPCmdEx(api, 0, Grab_X,  Grab_Y,  ColorSensor_Z, 0, 1)
