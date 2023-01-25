# Imports go at the top
from microbit import *
import radio
radio.config(group=255)
radio.on()
radio.send('hello') my_score = 10 
enemy_score = 0 def is_colliding(paddle_x, paddle_y, ball_x, ball_y):     pass paddle = [0, 0] 
