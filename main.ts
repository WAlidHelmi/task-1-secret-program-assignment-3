input.onButtonPressed(Button.A, function () {
    num1 += 1
    basic.showNumber(num1)
})
input.onButtonPressed(Button.AB, function () {
    if (num1 > player) {
        basic.showString("HIGHER")
    } else if (num1 < player) {
        basic.showString("lower")
    } else {
        basic.showString("Equal")
    }
})
input.onButtonPressed(Button.B, function () {
    num1 += -1
    basic.showNumber(num1)
})
let num1 = 0
let player = 0
basic.showIcon(IconNames.Asleep)
player = randint(0, 20)
