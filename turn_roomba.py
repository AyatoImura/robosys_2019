#!/usr/bin/env python
import roslib; roslib.load_manifest('beginner_tutorials')
import rospy

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

# stop robot immediately and report odometory
def stop_and_report():
    global g_odom
    pub = rospy.Publisher('cmd_vel', Twist)
    
    twist = Twist() # generate "STOP" condition twist data
    pub.publish(twist)
    rospy.sleep(1)
    print "Stopped"
    print "POS X:%2.3f" %g_odom.pose.pose.position.x,"POS Y:%2.3f" %g_odom.pose.pose.position.y,"DIR:%2.3f" %g_odom.pose.pose.orientation.z

# testing roomba movement and chaking odometory information
def mover():
    pub = rospy.Publisher('cmd_vel', Twist)
    
    # init node
    rospy.init_node('rb_demo')
    rospy.sleep(1) # waiting for init process is done
    
    # left turn
    print "Turning the robot left."
    twist = Twist();
    twist.angular.z = 1.0
    pub.publish(twist)
    
    # exit process
    print "Node exiting."

# copying odometory data to global var g_odom
def rb_callback(new_odom):
    global g_odom
    g_odom = new_odom

# main
if __name__ == '__main__':

    g_odom = 0 # storeing odometory information by callback function   
    rospy.Subscriber('odom', Odometry, rb_callback) # define callback function

    try:
        mover()
    except rospy.ROSInterruptException: 
        pass
