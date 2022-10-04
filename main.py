def on_button_pressed_a():
    global num1
    num1 += 1
    basic.show_number(num1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global num1
    if num1 > player:
        num1 += -1
        basic.show_number(num1)
    if num1 < player:
        num1 += 1
        basic.show_number(num1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global num1
    num1 += -1
    basic.show_number(num1)
input.on_button_pressed(Button.B, on_button_pressed_b)

num1 = 0
player = 0
basic.show_icon(IconNames.ASLEEP)
player = randint(0, 20)