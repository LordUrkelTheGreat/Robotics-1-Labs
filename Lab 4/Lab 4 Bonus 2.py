#Magician
for count in range(1):
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 160,  0,  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 9.24611274, 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  (-43), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  (-35),  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  (-35),  (-43), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  (-35),  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  (-43), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 180,  (-35),  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 180,  (-35),  (-45), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 180,  (-35),  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  (-43), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  0,  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  0,  (-43), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  0,  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  (-43), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 180,  0,  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 180,  0,  (-45), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 180,  0,  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)

  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 160,  0,  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 9.24611274, 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  (-43), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  (-35),  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  (-35),  (-16), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  (-35),  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  (-43), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 180,  (-35),  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 180,  (-35),  (-18), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 180,  (-35),  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  (-43), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  0,  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  0,  (-16), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  0,  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  (-43), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 215,  35,  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 180,  0,  20, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 180,  0,  (-18), current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 180,  0,  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.dSleep(2000)