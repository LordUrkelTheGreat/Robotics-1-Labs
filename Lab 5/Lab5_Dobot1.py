Calibration__0__Run__1 = None
Calibration_X = None
Calibration_Y = None
Calibration_Z = None
Place_X = None
Place_Y = None
Place_Z = None
j = None
k = None
time_start = None


print('[HOME] Restore to home position at first launch, please wait 30 seconds after turnning on the Dobot Magician.')
print('[BLOCKS] Place them besides the non-motor side of the conveyor belt, the same side where the pick and place arm is.')
print('[PLACING BLOCKS] Place the blocks by 3×3.')
print('[CALIBRATION POINT] Looking from the back of Dobot, the top left block is the calibration point.')
print('[CALIBRATION] Set the first variable to 0 to test the calibration point, then set 1 to start running.')
print('[DIRECTION] Standing behind Dobot Magician facing its front direction, X is front and back direction, Y is left and right direction. ')
print('[CONNECTION] Motor of the conveyor belt connects to port Stepper1.')
Calibration__0__Run__1 = 1
Calibration_X = 178
Calibration_Y = 220
Calibration_Z = -40
Place_X = 265
Place_Y = 17
Place_Z = 11
dType.SetEndEffectorParamsEx(api, 59.7, 0, 0, 1)
j = 0
k = 0
dType.SetPTPJointParamsEx(api,400,400,400,400,400,400,400,400,1)
dType.SetPTPCommonParamsEx(api,90,90,1)
dType.SetPTPJumpParamsEx(api,40,100,1)
dType.SetPTPCmdEx(api, 0, Calibration_X,  Calibration_Y,  Calibration_Z, 0, 1)
dType.SetEndEffectorSuctionCupEx(api, 0, 1)
STEP_PER_CRICLE = 360.0 / 1.8 * 10.0 * 16.0
MM_PER_CRICLE = 3.1415926535898 * 36.0
vel = float(0) * STEP_PER_CRICLE / MM_PER_CRICLE
dType.SetEMotorEx(api, 0, 0, int(vel), 1)
if Calibration__0__Run__1:
  for count in range(9):
    dType.SetPTPCmdEx(api, 0, (Calibration_X - j),  (Calibration_Y - k),  (Calibration_Z - 10), 0, 1)
    dType.SetEndEffectorSuctionCupEx(api, 1, 1)
    dType.dSleep(500)
    dType.SetPTPCmdEx(api, 0, Place_X,  Place_Y,  Place_Z, 0, 1)
    dType.SetEndEffectorSuctionCupEx(api, 0, 1)
    dType.dSleep(500)
    j = j + 25
    if j == 75:
      k = k + 25
      j = 0
    dType.SetPTPCmdEx(api, 7, 0,  0,  20, 0, 1)
    time_start = dType.gettime()[0]
    STEP_PER_CRICLE = 360.0 / 1.8 * 10.0 * 16.0
    MM_PER_CRICLE = 3.1415926535898 * 36.0
    vel = float(35) * STEP_PER_CRICLE / MM_PER_CRICLE
    dType.SetEMotorEx(api, 0, 1, int(vel), 1)
    while True:
      if (dType.gettime()[0]) - time_start >= 7:
        STEP_PER_CRICLE = 360.0 / 1.8 * 10.0 * 16.0
        MM_PER_CRICLE = 3.1415926535898 * 36.0
        vel = float(0) * STEP_PER_CRICLE / MM_PER_CRICLE
        dType.SetEMotorEx(api, 0, 0, int(vel), 1)
        break
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.SetPTPCmdEx(api, 0, Calibration_X,  Calibration_Y,  Calibration_Z, 0, 1)
