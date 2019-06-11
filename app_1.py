#######
# Author: James Poole
# Date: 23 April 2016
# jgaple@gmail.com
#
# Adapted for Adafruit motor shield
# Author: Pablo J. Rogina
# Date: 26 May 2016
# pablojr@gmail.com
#
# app.py
#######


use_mshield = True

from flask import Flask, render_template, request, redirect, url_for, make_response
if use_mshield:
    import mshield as motors
    motors.enable()
else:
    import motors
    import RPi.GPIO as GPIO

app = Flask(__name__) #set up flask server

#when the root IP is selected, return index.html page
print("ANTES DE IR A LA PAGINA")
@app.route('/')
#@app.route("/index")
def index():

        #return "HOLA MUNDO"

	return render_template('index.html')

#recieve which pin to change from the button press on index.html
#each button returns a number that triggers a command in this function
#
#Uses methods from motors.py to send commands to the GPIO to operate the motors
@app.route("/<changepin>", methods=["POST"])
def reroute(changepin):

	changePin = int(changepin) #cast changepin to an int

	if changePin == 1:
	    motors.turnLeft()
	elif changePin == 2:
            motors.forward()
	elif changePin == 3:
	    motors.turnRight()
	elif changePin == 4:
	    motors.backward()
	else:
	    motors.stop()


	response = make_response(redirect(url_for("index")))
	return(response)

# set up the server linstening on ort 8765
app.run(debug=False, host="192.168.0.58", port=8080) 

motors.disable()


