#!/usr/bin/env python

import math
import time
import moveit_commander
import rospy
import geometry_msgs.msg
import copy
import tf2_ros
import tf
from std_msgs.msg import Int32
from ar_pose.msg import ARMarker


def callback(message):
    print message.pose.pose.position.x

def main():
    rospy.init_node('ar_lisner')
    sub = rospy.Subscriber('/ar_pose_marker',ARMarker)

    tf_buffer = tf2_ros.Buffer()
    tf_listner = tf2_ros.TransformListener(tf_buffer)
    get_tf_flg = False

    count = 0
    while not get_tf_flg :
        try :
            print "count = ",count
            count =count+1
            start = time.time()
            time.sleep(1)
            trans = tf_buffer.lookup_transform('world', 'ar_marker', rospy.Time(0),rospy.Duration(10))
            print trans.transform
            elapsed_time = time.time() - start
            print "time = " ,elapsed_time
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) :
            continue

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
