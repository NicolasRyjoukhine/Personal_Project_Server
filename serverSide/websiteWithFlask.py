from flask import Flask, render_template, request
import json
import os

from serverSide.arduinoConnection.recieveAnalog import ObjectsDetected
from serverSide.arduinoConnection.sendAnalog import Move

template_dir = os.path.abspath('../clientSide/templates')
app = Flask(__name__, template_folder=template_dir)
move = Move(None, None, None)
objects = ObjectsDetected(9600).returnList()[0]
angles = ObjectsDetected(9600).returnList()[1]


@app.route('/home')
def mainhomescreen():
    button_val_left_right = ''
    button_val_up_down = ''
    button_int = 0
    angle_up_down_arm_1 = 0
    angle_up_down_arm_2 = 0
    angle_up_down_arm_3 = 0
    angle_base = 0
    is_gripping = False
    if request.method == "POST":
        if request.form["button_left"] == "Move Left":
            button_val_left_right = "BASE_MOVE_LEFT"
            angle_base -= 1
        if request.form["button_right"] == "Move Right":
            button_val_left_right = "BASE_MOVE_RIGHT"
            angle_base += 1
        if request.form["button_up"] == "Move Up":
            button_val_up_down = "ARM_MOVE_UP"
        if request.form["button_down"] == "Move Down":
            button_val_up_down = "ARM_MOVE_DOWN"
        if request.form["ARM_1"] == "ARM_1":
            button_int = 1
        if request.form["ARM_2"] == "ARM_2":
            button_int = 2
        if request.form["ARM_3"] == "ARM_3":
            button_int = 3
        if request.form["GRIP"] == "GRIP_ON":
            is_gripping = True
        elif request.form["GRIP"] == "GRIP_OFF":
            is_gripping = False

        print('Move right-left = {}\nMove Up Down = {}\n Selected Arm = {}'
              .format(button_val_left_right, button_val_up_down, button_int))
        move.moveBase(button_val_left_right)
        ##move.moveArm()

    return render_template('mainWithVideo.html',
                           armnum = button_int,
                           objects=objects,
                           angles=angles,
                           buttonint=angle_base)

@app.route('/about')
def aboutscreen():
    return render_template('mainWithVideo.html')

@app.route('/settings')
def settingscreen():
    return render_template('mainWithVideo.html')



app.run(debug=True)
