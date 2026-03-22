/* Copyright (c) 2026 MTHS All rights reserved
 *
 * Created by: Jayden Okafor
 * Created on: Mar 2026
 * This program measures the distance using the sonar.
*/

// variable
let distanceToObject:number = 0
basic.clearScreen()

basic.showIcon(IconNames.Happy)

input.onButtonPressed(Button.A, function() {
    basic.clearScreen()

    distanceToObject = sonar.ping(
       DigitalPin.P1,
       DigitalPin.P2,
       PingUnit.Centimeters,
    )
    
basic.showNumber(distanceToObject)
basic.showIcon(IconNames.Happy)
})


