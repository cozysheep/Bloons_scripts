import pynput
from time import sleep

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

def monkey_sub(x,y):
    mouse.position = (x,y)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)

    sleep(0.1)
    keyboard.press('x')
    keyboard.release('x')
    sleep(0.1)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)
    sleep(0.1)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)
    sleep(0.1)
    
    for i in range(2):
        keyboard.press(',')
        keyboard.release(',')
        sleep(0.1)
    for i in range(4):
        keyboard.press('/')
        keyboard.release('/')
        sleep(0.1)

def monkey_wizard(x,y):
    mouse.position = (x,y)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)

    sleep(0.1)
    keyboard.press('a')
    keyboard.release('a')
    sleep(0.1)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)
    sleep(0.1)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)
    sleep(0.1)
    
    for i in range(2):
        keyboard.press('/')
        keyboard.release('/')
        sleep(0.1)
    for i in range(3):
        keyboard.press('.')
        keyboard.release('.')
        sleep(0.1)

def main():
    monkey_sub(472,819)
    monkey_sub(1202,300)
    monkey_wizard(844,740)
    monkey_wizard(845,394)
    for i in range(2):
        keyboard.press(pynput.keyboard.Key.space)
        keyboard.release(pynput.keyboard.Key.space)
        sleep(0.1)
        
    sleep(41)
    
    # NEXT
    mouse.position = (971,941)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)
    sleep(0.7)
    
    # FREEPLAY
    mouse.position = (1226,882)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)
    sleep(0.7)
    
    # OK
    mouse.position = (971, 791)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)
    sleep(0.7)
    
    # RESTART
    keyboard.press(pynput.keyboard.Key.esc)
    keyboard.release(pynput.keyboard.Key.esc)
    sleep(1)
    mouse.position = (1085,877)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)
    sleep(0.7)
    
    # CONFIRM RESTART
    mouse.position = (1151,756)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)
    sleep(0.7)
    
for i in range(35):
    main()
