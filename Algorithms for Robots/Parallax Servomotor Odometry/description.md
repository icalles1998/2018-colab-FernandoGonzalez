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
  
# Code Explanation:
