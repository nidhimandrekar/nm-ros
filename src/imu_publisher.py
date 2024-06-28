
#!/usr/bin/env python2

import rospy
import rospkg
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion, Vector3

print("works") 

def imu_publisher():
    rospy.init_node('imu_publisher', anonymous=True)
    pub = rospy.Publisher('imu/data', Imu, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    # Create an Imu message
    imu_msg = Imu()
    imu_msg.header.frame_id = 'base_imu_link'

    # Set orientation (quaternion)
    imu_msg.orientation = Quaternion(x=0.1, y=0.2, z=0.3, w=0.4)

    # Set angular velocity
    imu_msg.angular_velocity = Vector3(x=0.1, y=0.2, z=0.3)

    # Set linear acceleration
    imu_msg.linear_acceleration = Vector3(x=0.5, y=0.6, z=0.7)

    while not rospy.is_shutdown():
        imu_msg.header.stamp = rospy.Time.now()
        pub.publish(imu_msg)
        rate.sleep()
print("works8")

if __name__ == '__main__':
    try:
        imu_publisher()
    except rospy.ROSInterruptException:
        pass

 