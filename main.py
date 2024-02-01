def on_button_pressed_a():
    global IsDrivingEnabled
    IsDrivingEnabled = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global IsDrivingEnabled
    IsDrivingEnabled = False
input.on_button_pressed(Button.B, on_button_pressed_b)

IsDrivingEnabled = False
fwdMotors.setup_driving(fwdMotors.left_servo, fwdMotors.right_servo, 0)

def on_forever():
    if IsDrivingEnabled:
        if fwdSensors.sonar1.fwd_distance_past_threshold(0.5, fwdSensors.ThresholdDirection.UNDER):
            fwdMotors.stop()
            basic.pause(1000)
            fwdMotors.drive(fwdMotors.DrivingDirection.REVERSE, 50)
            basic.pause(1000)
            fwdMotors.turn(25)
            basic.pause(1000)
        else:
            fwdMotors.drive(fwdMotors.DrivingDirection.FORWARD, 50)
    else:
        fwdMotors.stop()
basic.forever(on_forever)
