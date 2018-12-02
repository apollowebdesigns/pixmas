from flask import Flask, render_template, jsonify
app = Flask(__name__)
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause

class Tree():
    def __init__(self):
        self.on = False
        self.breaker = None

    def setLights(self):
        tree = LEDBoard(*range(2,28),pwm=True)
        for led in tree:
            led.source_delay = 0.1
            led.source = random_values()
            if(self.on == False):
                break

        pause()

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.off = False

tree = Tree()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/on')
def start():
    tree.setLights()
    return jsonify('done')

@app.route('/off')
def stop():
    tree.turnOff()
    return jsonify('done')

if __name__ == '__main__':
   app.run(host= '0.0.0.0')