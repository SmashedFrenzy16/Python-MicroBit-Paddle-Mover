# Imports go at the top
from microbit import *
import radio
radio.config(group=255)
radio.on()
radio.send('hello') 
my_score = 10 
enemy_score = 0 
paddle = [0, 0] 
def moving():     
  try:         
    if button_a.is_pressed() and paddle[1] != 5:
      display.clear()
      paddle[0] -= 1
      for i in range(5):
        display.set_pixel(0, paddle[0], 9)
        sleep(50)
    if button_b.is_pressed() and paddle[1] != 5:
      display.clear()
      paddle[0] += 1
      for i in range(5):
        display.set_pixel(0, paddle[0], 9)
        sleep(50)
  except ValueError:
    if paddle[0] > 0:             
      paddle[0] = 5         
    elif paddle[0] < 4:             
      paddle[0] = -1
# Code in a 'while True:' loop repeats forever
while True:
  moving()
