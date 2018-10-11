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
    
    #Import libraries:
    import RPi.GPIO as GPIO
    import time
   The "RPi.GPIO" library allows us to control the GPIO pins of the Raspberry Pi. On the other hand, "time" library is also needed but we will see it later.
   
   Now there are some parameters I'm going to comment:
   
## Constants:
   * ``DcMin = 29``
   * ``DcMax = 971``
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
    angle = initangle()
    p_angle = angle #We define a previous angle 
  ```
  At sentence ``angle  = initangle()`` we are calling to function "initangle" and we are saving in parameter "angle" what it returns and, in the next one, we are assigning his value to p_angle.
  
  Well, I think has arrive the moment to explain the function "initangle":
  ```
  def initangle():
    timeHigh = pulse_in(Encoder, 1) #Returns the time in microseconds
    timeLow = pulse_in(Encoder, 0)
    timeCycle = timeHigh + timeLow #I calculate the time cycle
    dutyCycle = (DutyScale * timeHigh) / timeCycle #I calculate the duty cycle
    return (FullCircle - 1) - ((dutyCycle - DcMin) * FullCircle) / (DcMax - DcMin + 1)
  
  ```
