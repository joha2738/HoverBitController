radio.onReceivedValueDeprecated(function (name, value) {
    if (name == "x") {
        xValue = value
    } else {
        if (name == "y") {
            yValue = value
        }
    }
})
let rightWheel = 0
let leftWheel = 0
let yValue = 0
let xValue = 0
basic.showIcon(IconNames.House)
radio.setGroup(1)
xValue = 0
yValue = 0
basic.forever(function () {
    leftWheel = yValue + xValue
    rightWheel = yValue - xValue
    if (leftWheel > 0) {
        kitronik.motorOn(kitronik.Motors.Motor1, kitronik.MotorDirection.Forward, leftWheel)
    } else {
        kitronik.motorOn(kitronik.Motors.Motor1, kitronik.MotorDirection.Reverse, Math.abs(leftWheel))
    }
    if (rightWheel > 0) {
        kitronik.motorOn(kitronik.Motors.Motor2, kitronik.MotorDirection.Forward, rightWheel)
    } else {
        kitronik.motorOn(kitronik.Motors.Motor2, kitronik.MotorDirection.Reverse, Math.abs(rightWheel))
    }
})
