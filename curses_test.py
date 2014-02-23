# PiBot control interface by Henry Plumb (henry@android.net)

import RPIO
import time
from Adafruit_PWM_Servo_Driver import PWM
import curses
import os

# Start mjpgstreamer webcam stream
os.system("sudo /home/pi/PiBot/start_stream.sh")

# Disable GPIO warning messages
RPIO.setwarnings(False)

# Setup motor outputs
RPIO.setup(7, RPIO.OUT)
RPIO.setup(8, RPIO.IN)
RPIO.setup(24, RPIO.OUT)
RPIO.setup(28, RPIO.OUT)
RPIO.setup(29, RPIO.OUT)
RPIO.setup(30, RPIO.OUT)
RPIO.setup(31, RPIO.OUT)

# Setup I2C servo driver
pwm = PWM(0x40, debug=True)
pwm.setPWMFreq(60)

# Curses intial setup
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.nodelay(1)

forward = False

def collision():
	time.sleep(0.055)
	RPIO.output(7, True)
	time.sleep(0.0001)
	RPIO.output(7, False)
	start = time.time()
	while not RPIO.input(8):
	        start = time.time()
	while RPIO.input(8):
	        stop = time.time()
	distance = ((stop - start) * 34000) / 2
	if distance >= 16:
		return False
	else:
		screen.addstr(0, 0, "Emergency Stop! Collision Imminent!")
		return True

def drive(dir):
	global forward
	if dir == "forward":
		forward = True
		RPIO.output(28, True)
		RPIO.output(29, False)
		RPIO.output(30, False)
		RPIO.output(31, True)
	if dir == "reverse":
		forward = False
		RPIO.output(28, False)
		RPIO.output(29, True)
		RPIO.output(30, True)
		RPIO.output(31, False)
	elif dir == "left":
		forward = False
		RPIO.output(28, True)
		RPIO.output(29, False)
		RPIO.output(30, True)
		RPIO.output(31, False)
	elif dir == "right":
		forward = False
		RPIO.output(28, False)
		RPIO.output(29, True)
		RPIO.output(30, False)
		RPIO.output(31, True)
	elif dir == "stop":
		forward = False
		RPIO.output(28, False)
		RPIO.output(29, False)
		RPIO.output(30, False)
		RPIO.output(31, False)

def checkkey():
        char = screen.getch()
        if char == curses.KEY_UP:
		drive("forward")
        elif char == curses.KEY_DOWN:
                drive("stop")
        elif char == curses.KEY_LEFT:
                drive("left")
        elif char == curses.KEY_RIGHT:
                drive("right")
        elif char == ord('r'):
                drive("reverse")

try:
	while True:
		checkkey()
		if collision() == True and forward == True:
			drive("stop")
		screen.refresh()
except KeyboardInterrupt:
	# Close curses cleanly
	curses.nocbreak()
	screen.keypad(0)
	curses.echo()
	curses.endwin()
	# Revert all GPIOs to outputs
	RPIO.cleanup()
	# Stop webcam stream
	os.system("sudo /home/pi/PiBot/stop_stream.sh")
