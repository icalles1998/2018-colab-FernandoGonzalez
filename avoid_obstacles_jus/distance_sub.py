#Este programa se subscribe al nodo distance para recibir la distancia del sensor
import rospy
import maestro as m
from std_msgs.msg import Int32

s = m.Controller()

def callback1(data):
    #rospy.loginfo(rospy.get_caller_id() + " %d received", data.data)
    s.setTarget(5, data.data)

def callback2(data):
    #rospy.loginfo(rospy.get_caller_id() + " %d received", data.data)
    s.setTarget(4, data.data)

if __name__ == '__main__':
    try:
       rospy.init_node('distance_sub', anonymous=False)

       rospy.Subscriber('/message1', Int32, callback1)

       rospy.Subscriber('/message2', Int32, callback2)

       rospy.spin()

    except rospy.ROSInterruptException:
        pass
