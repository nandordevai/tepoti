import time
import math
import os
import sys

def notify(title, text):
    os.system("""
osascript -e 'display notification "{}" with title "{}"'
""".format(text, title))
    
def get_time(seconds):
    return (math.floor(seconds / 60), seconds % 60)
    
def format_time(min, sec):
    return str(min).rjust(2, '0') + ':' + str(sec).rjust(2, '0')

def show_pomodoro():
    show_timer('Pomodoro', 1500)

def show_break():
    show_timer('Break', 300)

def show_timer(msg, seconds):
    for i in range(0, seconds):
        print(msg, format_time(*get_time(i)), ' ' * 10, end='\r', flush=True)
        time.sleep(1)
    notify('Pomodoro', '{} finished'.format(msg))


while True:
    try:
        show_pomodoro()
        show_break()
    except (KeyboardInterrupt):
        sys.exit(0)
