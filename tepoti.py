import time
import math
import os

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def getTime(seconds):
	return (math.floor(seconds / 60), seconds % 60)

def formatTime(min, sec):
	return str(min).rjust(2, '0') + ':' + str(sec).rjust(2, '0')

def show_pomodoro():
	show_timer('Pomodoro', 1200)

def show_break():
	show_timer('Break', 300)

def show_timer(msg, seconds):
	for i in range(0, seconds):
		print(msg, formatTime(*getTime(i)), ' ' * 10, end='\r', flush=True)
		time.sleep(1)
	notify('Pomodoro', '{} finished'.format(msg))


while True:
	show_pomodoro()
	show_break()

