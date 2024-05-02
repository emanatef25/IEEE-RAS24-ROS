#!/usr/bin/env python3
import rospy
from std_msgs.msg import String, Int16, Bool

def my_callback(my_string):
    rospy.loginfo("I heared %s", my_string.data)

def listener():
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber('chatter',String, my_callback)
    rospy.spin()
if __name__ == '__main__':
    try:
        listener()
    except rospy.ROInterruptException:
        pass