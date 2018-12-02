from flask import Flask, render_template, jsonify
app = Flask(__name__)
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause

class Tree():
    def __init__(self):
        self.on = False

    def setLights(self):
        if(self.on == True):
            tree = LEDBoard(*range(2,28),pwm=True)
            for led in tree:
                led.source_delay = 0.1
                led.source = random_values()
            pause()

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

tree = Tree()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/on')
def start():
    tree.turnOn()
    return jsonify('done')

@app.route('/off')
def stop():
    tree.turnOff()
    return jsonify('done')