#!/usr/bin/env python
import serial
import rospy
from std_msgs.msg import String

ser = serial.Serial('/dev/ttyUSB0', 19200)

def usbl_pub():
    pub = rospy.Publisher('chatter', String, queue_size=50)
    rospy.init_node('usbl_pub', anonymous=True)
    rate = rospy.Rate(10) # 10Hz
    rospy.loginfo("node usbl_pub set")
    while not rospy.is_shutdown():
        rospy.loginfo("in while")
        line = ser.readline()
        if line:
            rospy.loginfo("in if")
            data_list = line.split(",")
            hello_str = "hello world %s" % rospy.get_time()
            data_str = "data are: %s, %s, %s, %s" % (data_list[2], data_list[3], data_list[4], data_list[7])
            rospy.loginfo(data_str)
            rospy.loginfo(hello_str)
            pub.publish(data_str)
            rate.sleep()

if __name__ == '__main__':
    try:
        usbl_pub()
    except rospy.ROSInterruptException:
        pass
