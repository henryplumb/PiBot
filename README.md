PiBot
=====

Code for my Raspberry Pi Rover, PiBot. This uses Python Curses, allowing arrow key based control for movement and WAZDS control for camera pan/tilt.

Drive motors, by default, are connected to GPIO 28-31 (P5 header).

Collision avoidance uses an HC-SR04 ultrasonic range finder module.

Servos are controlled via the Adafruit 16-channel I2C Servo Driver for the Pi. This uses the Adafruit_PWM Library for control from within Python.

The shell scripts are run by the Python program using os.system() and start and stop the webcam stream using raspistill for images from the Raspberry Pi Camera being streamed through mjpg-streamer.

###GPIO Usage Summary:

GPIO 7 : INPUT : Echo from HC-SR04

GPIO 8 : OUTPUT : Trigger for HC-SR04


GPIO 24 : OUTPUT : Relay control for headlight


GPIO 28 : OUTPUT : Motor control 1

GPIO 29 : OUTPUT : Motor control 2

GPIO 30 : OUTPUT : Motor control 3

GPIO 31 : OUTPUT : Motor control 4


SDA (GPIO 2) : I2C : Servo driver

SDL (GPIO 3) : I2C : Servo driver
