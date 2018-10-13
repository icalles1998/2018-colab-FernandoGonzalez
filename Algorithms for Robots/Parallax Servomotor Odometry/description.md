# Introduction:
  This library is used to measure the odometry of the servomotor "Parallax feedback 360º".
  
# About Feedback Signal:
   Firt one, we need to undestand the operation of feedback signal.
  It is a PWM signal. What that means? PWM means "Pulse Width Modulation". It is a signal of information. 
  How this signal be able to transport information? Modulating his pulse width. Let's look an example:
  
  ![can not load the image](https://github.com/TheRoboticsClub/2018-colab-FernandoGonzalez/blob/master/docs/pwm_signal.png)
  
   So, the signal feedback will transport the information we need to know the angle of the servomotor at each instant.
   We can read this signal connecting the feedback cable that the servomotor provides to a GPIO pin of our Raspberry Pi.
   
   But we need to know to interpret the information that the signal provides us. How can we do this?
   
   Within each tCycle iteration, tHigh is the duration in microseconds of a 3.3 V high pulse. The duration of tHigh varies with  the  output  of  a  Hall-effect  sensor  inside  of  the  servo. The  duty  cycle  of  this  signal, tHigh / tCycle, ranges from 2.9% at the origin to 91.7% approaching one clockwise revolution.
   In the next image we can see other example of how the feedback signal is:
   
   ![can not load the image](https://github.com/TheRoboticsClub/2018-colab-FernandoGonzalez/blob/master/docs/feedback_signal.png)
   
   Duty cycle corresponds to the rotational position of the servo, in the units per full circle desired for your application.
   Duty Cycle = 100% x (tHigh / tCycle). Duty Cycle Min = 2.9%. Duty Cycle Max= 91.7%.
   The signal will vary in time, so we have to be reading the feedback signal every time.
  
# Code Explanation:

   At first, we need to import two python libraries:
    
    import RPi.GPIO as GPIO
    import time
   The "RPi.GPIO" library allows us to control the GPIO pins of the Raspberry Pi. On the other hand, "time" library is also needed but we will see it later.
   
   Now there are some parameters I'm going to comment:
   
## Constants:
   * ``DcMin = 29``=> Minumin duty cycle
   * ``DcMax = 971``=> Maximum duty cycle
   * ``Pi = 3.1416``
   * ``FullCircle = 2 * pi `` => Total angle of the circle. You can choose de measure (radians or degrees)
   * ``DutyScale = 1000`` =>Period of the signal
   * ``Q2Min = FullCircle / 4`` =>Minimun angle of second quadrant
   * ``Q3Max = Q2Min * 3`` =>Minimum angle of fourth quadrant
   * ``Encoder = 24`` =>feedback pin

  We have eight parameters that are considered constants becasue they don't vary. Only be able be changed one of them. Constant "FullCircle" defines the total angle if we considerate the full circle. You can work with radians or with degrees, dependin of you write '2 * Pi' or '360'. So, if you prefer work with degrees, you only have to change '2 * Pi' for '360'.
  
  We also can see the parameter 'turns'. This parameter will serve to us to know which direction is rotating the servomotor.
  * ``turns = 0``
      
  Let's continue commenting the code. Now, I'm going to skip part of the code so it can be well understood and we are going to look that sentences:
  ```
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(Encoder, GPIO.IN)
  ```
  ``GPIO.setmode(GPIO.BCM)`` serves to configure the way we are going to refer to the Raspberry Pi pins; and ``GPIO.setup(Encoder, GPIO.IN)`` is configuring the pin we named before "Encoder" as input pin. We need to do this to be able to read the signal.
  
  Now, let's start with the main algorithm:
  
  ```
    angle = initangle()
    p_angle = angle #We define a previous angle 
  ```
  At sentence ``angle  = initangle()`` we are calling to function "initangle" and we are saving in parameter "angle" what it returns and, in the next one, we are assigning his value to p_angle.
  
  Well, I think has arrive the moment to explain the function "initangle":
  ```
  def initangle():
    timeHigh = pulse_in(Encoder, 1)
    timeLow = pulse_in(Encoder, 0)
    timeCycle = timeHigh + timeLow
    dutyCycle = (DutyScale * timeHigh) / timeCycle #I calculate the duty cycle
    return (FullCircle - 1) - ((dutyCycle - DcMin) * FullCircle) / (DcMax - DcMin + 1)
  
  ```
  At first, we save  in the parameters 'timeHigh' with sentence ``timeHigh = pulse_in(Encoder, 1)`` and 'timeLow' with sentence ``timeLow = pulse_in(Encoder, 0)`` the time that signal is on High and Low. The Raspberry GPIO pins are digital, so, when signal is High, it is being receiving ones, and when signal is Low, it is being receiving zeros. the time signal is High or Low can be knows by the function 'pulse_in'. That function receive like paremeter, the Raspberry pin where it is being reading and, the bit wich represents the signal value we can measure (High = 1 and Low = 0). So, We are going to see how the function 'pulse_in' is.
At sentence ``dutyCycle = (DutyScale * timeHigh) / timeCycle`` we are calculating the duty cycle as quotient of 'timeHIGH' and 'timeCycle'. It is being multiplicated by 'DutyScale'. We have to remember 'DutyScale' is the signal period. 
Finally, we calculate the angle with the next formula: 

```(FullCircle - 1) - ((dutyCycle - DcMin) * FullCircle) / (DcMax - DcMin + 1)```
But, maybe yo are asking yourself why we have to calculate an init angle. on the rest of the code, we are calculating the angle in that the servomotor is comparing this one with the angle calculates previously. It's for that we need an init angle.
At next lines of code, we can observe a loop where in each iteration it is calculated a new angle of the same way than before except this two lines:
```
if((timeCycle > 1000) and (timeCycle < 1200)):
  finish = True
```
This condition serves to be sure time cycle is in a correct range. If it is like that, we let to calculate the duty cycle.
Later to calculate the new angle we can see a new condition:
```
if(angle < 0):
  angle = 0
elif(angle > (FullCircle - 1)):
  angle = FullCircle - 1

```
That condition simply serves to keep 'angle' into a range where his minimum value is 0 and his maximum value is 359 (because 360 is considered 0 for the next spin).
It is more interesting to analize the next lines:
```
if((angle < Q2Min) and (p_angle > Q3Max)):
  turns = turns + 1
elif((p_angle < Q2Min) and (angle > Q3Max)):
  turns = turns - 1
```
if servomotor turns in the clockwise, 'turns' increase, but if servomotor turns in the anticlockwise, then, turns decreases
