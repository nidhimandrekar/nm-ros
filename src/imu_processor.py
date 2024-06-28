#!/usr/bin/env python

import rospy
import rospkg
from sensor_msgs.msg import Imu
from std_msgs.msg import Float32

print("works")

def imu_callback(data):
    # Process your IMU data here
    # For example, let's say we want to publish the linear acceleration magnitude
    linear_acc_magnitude = (data.linear_acceleration.x ** 2 + 
                            data.linear_acceleration.y ** 2 + 
                            data.linear_acceleration.z ** 2) ** 0.5

    # Publish the processed data
    pub.publish(linear_acc_magnitude)

if __name__ == '__main__':
    rospy.init_node('imu_processor', anonymous=True)

    # Subscriber to IMU topic
    rospy.Subscriber('imu/data', Imu, imu_callback)

    # Publisher for processed data
    pub = rospy.Publisher('imu/processed_data', Float32, queue_size=10)
    rospy.spin()
