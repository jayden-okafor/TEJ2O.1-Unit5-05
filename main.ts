/* Copyright (c) 2026 MTHS All rights reserved
 *
 * Created by: Jayden Okafor
 * Created on: Mar 2026
 * This program measures the distance using the sonar.
*/

// variable
let distanceToObject:number = 0 
basic.clearScreen()

// show happy face
basic.showIcon(IconNames.Happy)

// when button "A" is clicked
input.onButtonPressed(Button.A, function() {
    basic.clearScreen()

// measure the distance in cm
    distanceToObject = sonar.ping(
       DigitalPin.P1, // trigger
       DigitalPin.P2, // echo
       PingUnit.Centimeters,
    )   
basic.showString(distanceToObject.toString() + ' cm')
basic.showIcon(IconNames.Happy)
})
