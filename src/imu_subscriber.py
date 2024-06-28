#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu

def imu_callback(data):
    # Process IMU data (example: print orientation)
    orientation = data.orientation
    rospy.loginfo("Received IMU data. Orientation: x={}, y={}, z={}, w={}".format(
        orientation.x, orientation.y, orientation.z, orientation.w))

def imu_listener():
    rospy.init_node('imu_listener', anonymous=True)
    rospy.Subscriber('imu/data', Imu, imu_callback)
    rospy.spin()

if __name__ == '__main__':
    imu_listener()
