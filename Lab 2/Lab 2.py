#Magician
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], 60, 1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 250,  10,  75, current_pose[3], 1)
dType.SetEndEffectorGripperEx(api, 1, 1)
dType.dSleep(2000)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 200,  60,  75, current_pose[3], 1)
dType.SetEndEffectorGripperEx(api, 1, 0)
dType.dSleep(2000)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 200,  60,  (-25), current_pose[3], 1)
dType.SetEndEffectorGripperEx(api, 1, 1)
dType.dSleep(2000)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 200,  60,  75, current_pose[3], 1)
dType.SetEndEffectorGripperEx(api, 1, 1)
dType.dSleep(2000)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 200,  (-60),  75, current_pose[3], 1)
dType.SetEndEffectorGripperEx(api, 1, 1)
dType.dSleep(2000)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 200,  (-60),  (-25), current_pose[3], 1)
dType.SetEndEffectorGripperEx(api, 1, 0)
dType.dSleep(2000)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 200,  (-60),  75, current_pose[3], 1)
dType.SetEndEffectorGripperEx(api, 1, 0)
dType.dSleep(2000)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 250,  10,  75, current_pose[3], 1)
dType.SetEndEffectorGripperEx(api, 1, 1)
dType.dSleep(2000)
