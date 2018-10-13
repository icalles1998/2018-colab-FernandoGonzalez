#! /usr/bin/env python
#Import libraries:
import RPi.GPIO as GPIO
import time

#Constants:
DcMin = 29 #Minimun duty cycle
DcMax = 971 #Maximum duty cycle
Pi = 3.1416
FullCircle = 2 * pi #Total angle of the circle. You can choose de measure (radians or degrees)
DutyScale = 1000 #Period of the signal
Q2Min = FullCircle / 4 #Minimun angle of second quadrant
Q3Max = Q2Min * 3 #Minimum angle of fourth quadrant
Encoder = 24 #feedback pin

turns = 0 #This parameter will serve us to know the direction of rotation of servo


def pulse_in(inp, bit):

    def readuntil(inp, bit):
	rec = GPIO.input(inp)
	if(rec == bit):
	    #Wait until finish reading ones
	    while(rec == bit):
		rec = GPIO.input(inp)
	#Read zeros until receive the first "one"
	if(bit == 1):
	    while(rec == 0):
		rec = GPIO.input(inp)
        #It have just arrived the first "one" after zeros
	else:
	    while(rec == 1):
		rec = GPIO.input(inp)
        #It have just arrived the first zero after ones

    if(bit != 0 and bit != 1):
	    return 0
    else:
    	readuntil(inp, bit) #I read until arrive the next bit
    	start = time.time() #I save the actual hour
	if(bit == 1):
	    readuntil(inp, 0) #I read until arrive a contrary bit to the before one
	else:
	    readuntil(inp, 1)
	finish = time.time()
	elapsed = (finish - start) * 1000000 #time in microseconds

	return elapsed

def initangle():
    timeHigh = pulse_in(Encoder, 1) #Returns the time in microseconds
    timeLow = pulse_in(Encoder, 0)
    timeCycle = timeHigh + timeLow #I calculate the time cycle
    dutyCycle = (DutyScale * timeHigh) / timeCycle #I calculate the duty cycle
    return (FullCircle - 1) - ((dutyCycle - DcMin) * FullCircle) / (DcMax - DcMin + 1)

#It is initialized the feedback pin configuration:
GPIO.setmode(GPIO.BCM)
GPIO.setup(Encoder, GPIO.IN)

try:

    #I calculate the initial angle
    angle = initangle()
    p_angle = angle #We define a previous angle

    while(True):

    	finish = False
    	while(not finish):
    	    timeHigh = pulse_in(Encoder, 1) #Returns the time in microseconds
    	    timeLow = pulse_in(Encoder, 0)

    	    timeCycle = timeHigh + timeLow #I calculate the time cycle

    	    if((timeCycle > 1000) and (timeCycle < 1200)):
    		          finish = True

    	dutyCycle = (DutyScale * timeHigh)/ timeCycle #I calculate the duty cycle

    	angle = (FullCircle - 1) - ((dutyCycle - DcMin) * FullCircle) / (DcMax - DcMin + 1) #Calculate angle
        #Keep angle inside the allow range
        if(angle < 0):
    	    angle = 0
    	elif(angle > (FullCircle - 1)):
    	    angle = FullCircle - 1

        #If transition from quadrant 4 to quadrant 1, increase turns count.
        if((angle < Q2Min) and (p_angle > Q3Max)):
          turns = turns + 1
        #If transition from quadrant 1 to  quadrant 4, decrease turns count.
	    elif((p_angle < Q2Min) and (angle > Q3Max)):
          turns = turns - 1

        #Construct the angle measurement from the turns count and current angle value.
        if(turns >= 0):
          angle = (turns * FullCircle) + angle
        elif(turns <  0):
          angle = ((turns + 1) * FullCircle) - (FullCircle - angle)

        #If it is completed a full turn, the angle returns to zero
	    if(angle >= FullCircle):
    	    angle = angle - FullCircle
    	    turns = 0
    	elif(angle <= -FullCircle):
    	    angle = angle + FullCircle
    	    turns = 0
    	#Uncomment to print the angle:
	#print(angle)

    	#uncomment to return the angle
    	#return angle
	p_angle = angle
    	time.sleep(0.001)

except KeyboardInterrupt:
	pass
