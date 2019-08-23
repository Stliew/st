#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from darknet_ros_msgs.msg import BoundingBoxes




def person_center(data):
    for i in data.bounding_boxes:
        if i.Class=='car':
            center_x = (i.xmin + i.xmax)/2
            center_y = (i.ymin + i.ymax)/2
            print('center_x:',center_x)
            print('name=',i.Class)
            print('helo')
            rospy.loginfo("center_y: %s",center_y)


          


    

def apriltag_callback():
    rospy.init_node('apriltag_callback', anonymous=True)

    rospy.Subscriber("/darknet_ros/bounding_boxes",BoundingBoxes,person_center )

    rospy.spin()




if __name__ == '__main__':
    apriltag_callback()
    