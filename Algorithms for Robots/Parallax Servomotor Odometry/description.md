# Introduction:
  This library is used to measure the odometry of the servomotor "Parallax feedback 360º".
  
# About Feedback Signal:
   Firt one, we need to undestand the operation of feedback signal.
  It is a PWM signal. What that means? PWM means "Pulse Width Modulation". It is a signal of information. 
  How this signal be able to transport information? Modulating his pulse width. Let's look an example:
  
  ![](https://github.com/TheRoboticsClub/2018-colab-FernandoGonzalez/blob/master/docs/pwm_signal.png)
  
   So, the signal feedback will transport the information we need to know the angle of the servomotor at each instant,
   but we need to know to interpret the information that the signal provides us. How can we do this?
  
# Code Explanation:
