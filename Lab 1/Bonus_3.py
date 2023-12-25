#Magician
import math

dType.SetJOGJointParams(api, 150, 150, 150, 150, 150, 150, 150, 150, 0)

for count in range(1):
    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, 250,  60,  (-8), current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, 250,  60,  (-90), current_pose[3], 1)

    dType.SetJOGCmd(api, 1, 1, 1)
    dType.SetWAITCmd(api, 500, 1)
    dType.SetJOGCmd(api, 1, 0, 1)
    dType.SetWAITCmd(api, 200, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, 156.5273,  203.9589,  (-8), current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, 156.5273,  213.9589,  (-8), current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, 156.5273,  213.9589,  (-90), current_pose[3], 1)

    dType.SetJOGCmd(api, 1, 2, 1)
    dType.SetWAITCmd(api, 500, 1)
    dType.SetJOGCmd(api, 1, 0, 1)
    dType.SetWAITCmd(api, 200, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, 256.2933,  67.7715,  (-8), current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, 256.2933,  77.7715,  (-8), current_pose[3], 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, 256.2933,  77.7715,  (-90), current_pose[3], 1)

    dType.SetJOGCmd(api, 1, 1, 1)
    dType.SetWAITCmd(api, 500, 1)
    dType.SetJOGCmd(api, 1, 0, 1)
    dType.SetWAITCmd(api, 200, 1)

    current_pose = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, 150.2341,  221.7304,  (-8), current_pose[3], 1)

