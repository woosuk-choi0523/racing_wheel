import string
import vgamepad as vg
import serial
import time
import re

# 'COM3' 부분에 환경에 맞는 포트 입력
ser = serial.Serial('COM3', 9600)
gamepad = vg.VX360Gamepad()

while True:
    if ser.readable():
        temp = str(ser.readline())
        raw_data = temp[2:-5]
        temp2 = raw_data[0:-7]
        stearing = (float(re.sub(r'[^0-9]', '', temp2)) / 1023 - 0.5)*2
        temp3 = float(raw_data[-3])
        if(temp3 == 1):
            breakbtn = 0
        if(temp3 == 0):
            breakbtn = 1
        temp4 = float(raw_data[-1])
        if(temp4 == 1):
            accelerate = 0
        if(temp4 == 0):
            accelerate = 1
        print(stearing ,breakbtn , accelerate)
        gamepad.left_joystick_float(x_value_float=stearing, y_value_float=0)
        gamepad.left_trigger_float(value_float=breakbtn)
        gamepad.right_trigger_float(value_float=accelerate)
        gamepad.update()