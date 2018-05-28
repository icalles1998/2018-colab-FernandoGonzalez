#Este programa es el publicador de distancias que lee del el puerto serial (enviadas desde arduino)
import rospy
import time
import maestro
from std_msgs.msg import Int32
from std_msgs.msg import String

pololu = maestro.Controller()

sensor_dist = 0
a = 6787
b = 3
c = 4

pub1 = rospy.Publisher('/message1', Int32, queue_size = 1)
pub2 = rospy.Publisher('/message2', Int32, queue_size = 1)

try:
    def callback(data):
        motorL = -1
        if(data.data == 'a'):
            #read_distance(motorR, motorL)
            Output = pololu.getPosition(sensor_dist)
            dist = (a / (Output - b)) - c
            #print(dist)
            if(dist < 15):
               motorR = -1
            else:
               motorR = 1
        else:
            motorR = 0
            motorL = 0
        print(motorR)
        print(motorL)
        print("---")
        pub1.publish(motorR)
        pub2.publish(motorL)

    if(__name__ == '__main__'):
        rospy.init_node("distance_pub", anonymous = False)

        while(not rospy.is_shutdown()):

            rospy.Subscriber('/command', String, callback)
            rospy.spin()

except rospy.ROSInterruptException:
    pass
