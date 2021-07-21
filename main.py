def on_received_value_deprecated(name, value):
    global xValue, yValue
    if name == "x":
        xValue = value
    elif name == "y":
        yValue = value
radio.on_received_value_deprecated(on_received_value_deprecated)

rightWheel = 0
leftWheel = 0
yValue = 0
xValue = 0
basic.show_icon(IconNames.HOUSE)
radio.set_group(17)
xValue = 0
yValue = 0

def on_forever():
    global leftWheel, rightWheel
    leftWheel = yValue + xValue
    rightWheel = yValue - xValue
    if leftWheel > 0:
        kitronik.motor_on(kitronik.Motors.MOTOR1,
            kitronik.MotorDirection.FORWARD,
            leftWheel)
    else:
        kitronik.motor_on(kitronik.Motors.MOTOR1,
            kitronik.MotorDirection.REVERSE,
            abs(leftWheel))
    if rightWheel > 0:
        kitronik.motor_on(kitronik.Motors.MOTOR2,
            kitronik.MotorDirection.FORWARD,
            rightWheel)
    else:
        kitronik.motor_on(kitronik.Motors.MOTOR2,
            kitronik.MotorDirection.REVERSE,
            abs(rightWheel))
basic.forever(on_forever)
