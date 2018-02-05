#!/usr/bin/env python
import serial
import rospy
from std_msgs.msg import String

ser = serial.Serial('/dev/ttyUSB0', 19200)

def usbl_pub():
    # publishers
    pub1 = rospy.Publisher('relative_x', String, queue_size=10)
    pub2 = rospy.Publisher('relative_y', String, queue_size=10)
    pub3 = rospy.Publisher('relative_z', String, queue_size=10)
    pub4 = rospy.Publisher('usbl_time', String, queue_size=10)

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
            #rospy.loginfo(hello_str)
            pub1.publish(data_list[2])
            pub2.publish(data_list[3])
            pub3.publish(data_list[4])
            pub4.publish(data_list[7])
            rate.sleep()

if __name__ == '__main__':
    try:
        usbl_pub()
    except rospy.ROSInterruptException:
        pass
