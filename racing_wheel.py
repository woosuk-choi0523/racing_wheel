import string
import vgamepad as vg
import serial
import time
import re

ser = serial.Serial('COM3', 9600) # 'COM3' is arduino`s serial port`
gamepad = vg.VX360Gamepad()       # Starting vgamepad

while True:
    if ser.readable():  
        temp = str(ser.readline())
        raw_data = temp[2:-5].split()
        stearing = (float(re.sub(r'[^0-9]', '', raw_data[0]))/102300 -0.5)*2
        breakbtn = (float(re.sub(r'[^0-9]', '', raw_data[1]))-1)*-1
        breakbtn = (float(re.sub(r'[^0-9]', '', raw_data[2]))-1)*-1
        '''
        print(stearing ,breakbtn , accelerate)
        gamepad.left_joystick_float(x_value_float=stearing, y_value_float=0)
        gamepad.left_trigger_float(value_float=breakbtn)
        gamepad.right_trigger_float(value_float=accelerate)
        gamepad.update()
        
        '''