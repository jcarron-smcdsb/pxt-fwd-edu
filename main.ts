input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    IsDrivingEnabled = true
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    IsDrivingEnabled = false
})
let IsDrivingEnabled = false
fwdMotors.setupDriving(fwdMotors.leftServo, fwdMotors.rightServo, 0)
basic.forever(function on_forever() {
    if (IsDrivingEnabled) {
        if (fwdSensors.sonar1.fwdDistancePastThreshold(0.5, fwdSensors.ThresholdDirection.Under)) {
            fwdMotors.stop()
            basic.pause(1000)
            fwdMotors.drive(fwdMotors.DrivingDirection.Reverse, 50)
            basic.pause(1000)
            fwdMotors.turn(25)
            basic.pause(1000)
        } else {
            fwdMotors.drive(fwdMotors.DrivingDirection.Forward, 50)
        }
        
    } else {
        fwdMotors.stop()
    }
    
})
