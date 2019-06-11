#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    import RPi.GPIO as GPIO
    from flask import Flask, render_template, request, redirect, url_for, make_response
    import time
    from AMSpi import AMSpi
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. "
          "You can achieve this by using 'sudo' to run your script")

def ADELANTE():
        print("ADELANTE")
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])
        time.sleep(0.5)
def ATRAS():
        print("ATRAS")
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4], clockwise=False)
        time.sleep(0.5)
def DERECHA():
        print("DERECHA")
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])
        amspi.run_dc_motors([amspi.DC_Motor_3, amspi.DC_Motor_4], clockwise=False)
        time.sleep(0.5)
def IZQUIERDA():
        print("IZQUIERDA")
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2], clockwise=False)
        amspi.run_dc_motors([amspi.DC_Motor_3, amspi.DC_Motor_4])
        time.sleep(0.5)
def STOP():
        print("Stop")
        amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])
def EXIT():
        print("Stop and Exit")
        amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])

import Motores
if  __name__ == '__main__':
    with AMSpi() as amspi:    
        amspi.set_74HC595_pins(21, 20, 16)
        amspi.set_L293D_pins(5, 6, 13, 19)

        app = Flask(__name__) #set up flask server

        #when the root IP is selected, return index.html page
        @app.route('/')
        #@app.route("/index")
        def index():

            return render_template('index.html')

        #recieve which pin to change from the button press on index.html
        #each button returns a number that triggers a command in this function
        #
        #Uses methods from motors.py to send commands to the GPIO to operate the motors
        @app.route("/<changepin>", methods=["POST"])
        def reroute(changepin):

            changePin = int(changepin) #cast changepin to an int

            if changePin == 1:
                IZQUIERDA()
                STOP()
            elif changePin == 2:
                ADELANTE()
                STOP()
            elif changePin == 3:
                DERECHA()
                STOP()
            elif changePin == 4:
                ATRAS()
                STOP()
            else:
                STOP()
                
            response = make_response(redirect(url_for("index")))
            return(response)

        # set up the server linstening on ort 8765
        app.run(debug=False, host="192.168.0.58", port=8080) 
