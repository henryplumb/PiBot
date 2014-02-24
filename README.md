PiBot
=====

Code for my Raspberry Pi Rover, PiBot.

Servos are controlled via the Adafruit 16-channel I2C Servo Driver for the Pi. This uses the Adafruit_PWM Library for control from within Python.

The shell scripts are run by the Python program using os.system and start and stop the webcam stream using raspistill for images from the Raspberry Pi Camera being streamed through mjpg-streamer.
