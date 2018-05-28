#Recoge datos desde arduino
import serial
import rospy
import time
from std_msgs.msg import String

ser = serial.Serial("/dev/ttyACM0", 9600)

try:

    if(__name__ == '__main__'):
        rospy.init_node("command_receiver", anonymous = False)

        pub = rospy.Publisher('/command', String, queue_size = 1)

    data = ser.read();
    while(data != "p"):
        data = ser.read();

    while(not rospy.is_shutdown()):
        data = ser.read()
        if(data == 'a' or data == 'p'):
            print(data)
            print("----")
            pub.publish(data)

except rospy.ROSInterruptException:
    pass
