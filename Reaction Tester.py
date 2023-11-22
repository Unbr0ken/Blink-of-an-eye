import time, random, _thread
from time import sleep
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P8

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P8, rotate=0)

display.set_backlight(0.5)
display.set_font("bitmap8")

#Creates Buttons
button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

#Creates Colors
RED = display.create_pen(209, 34, 41)
ORANGE = display.create_pen(246, 138, 30)
YELLOW = display.create_pen(255, 216, 0)
GREEN = display.create_pen(0, 228, 54)
INDIGO = display.create_pen(36, 64, 142)
VIOLET = display.create_pen(115, 41, 130)
WHITE = display.create_pen(255, 255, 255)
PINK = display.create_pen(255, 175, 200)
BLUE = display.create_pen(116, 215, 238)
BROWN = display.create_pen(97, 57, 21)
BLACK = display.create_pen(0, 0, 0)
MAGENTA = display.create_pen(255, 33, 140)
CYAN = display.create_pen(33, 177, 255)
DARKGREEN= display.create_pen(0, 135, 81)
PINK = display.create_pen(225, 119, 168)

colorList = [RED, ORANGE, INDIGO, VIOLET,PINK, BLUE, BROWN, WHITE, CYAN, MAGENTA, YELLOW, GREEN]

startingTime, endingTime = 0, 0

# Clears the screen to black
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()
    
clear()

# Creates Main Screen
def main():
    # Creates Game Title Screen
    clear()
    display.set_pen(GREEN)
    display.text("Blink of an Eye", 30, 25, 240, 5)
    display.update()
    time.sleep(2)
    clear()
    
    # Switches between two "screens" and allows buttons to be pressed
    while True:
        for i in range(10):
            if button_a.read():
                howToPlay()
            if button_b.read():
                play()
            display.set_pen(YELLOW)
            display.text('''How To Play: Press 'A' ''', 15, 35, 240, 4)
            display.update()
            time.sleep(0.1)
            clear()
        for i in range(10):
            if button_a.read():
                howToPlay()
            if button_b.read():
                play()
            display.set_pen(MAGENTA)
            display.text('''Play: Press 'B' ''', 15, 35, 240, 4)
            display.update()
            time.sleep(0.1)
            clear()
        
#Creates How to Play Screen
def howToPlay():
    clear()
    display.set_pen(YELLOW)
    display.text('''How To Play''', 15, 55, 240, 4)
    display.update()
    time.sleep(0.5)
    clear()
    
    display.set_pen(YELLOW)
    display.text('''A few colors will flash on the screen; the player should wait to press 'Y' until green appears.''', 10, 35, 230, 2.5)
    display.update()
    time.sleep(4)
    clear()
    
    display.set_pen(YELLOW)
    display.text('''When 'Y' is pressed, your reaction time will appear on the screen. To play again, press 'X', and 'A' to go back to the menu.''', 10, 20, 230, 2.5)
    display.update()
    time.sleep(5)
    clear()
    while True:
        display.set_pen(YELLOW)
        display.text('''Press 'B' To Play''', 25, 40, 230, 4)
        display.update()
        clear()
        if button_b.read():
            play()

#Creates the Game
def play():
    clear()
    screen = 0
    display.set_pen(PINK)
    display.text('''Playing''', 25, 50, 240, 6)
    display.update()
    time.sleep(0.5)
    clear()
    
    display.set_pen(PINK)
    display.text('''IN''', 100, 50, 240, 6)
    display.update()
    time.sleep(0.5)
    clear()
    
    display.set_pen(RED)
    display.text('''3''', 100, 50, 240, 6)
    display.update()
    time.sleep(0.5)
    clear()
    
    display.set_pen(ORANGE)
    display.text('''2''', 100, 50, 240, 6)
    display.update()
    time.sleep(0.5)
    clear()
    
    display.set_pen(YELLOW)
    display.text('''1''', 100, 50, 240, 6)
    display.update()
    time.sleep(0.5)
    clear()
    
    display.set_pen(DARKGREEN)
    display.text('''GO''', 100, 50, 240, 6)
    display.update()
    time.sleep(0.5)
    clear()
    
    # Switches between colors until it gets the green, where it stops and starts the timer
    while True:
        colors = random.choice(colorList)
        randomTime = random.uniform(0.5, 1)
        
        display.set_pen(colors)
        if colors == GREEN:
            startingTime= time.ticks_ms()
            print (startingTime)
        display.clear()
        display.update()
        if colors == GREEN:
            break
        sleep(randomTime)
        clear()
    while True:
        if button_y.read():
            if colors == GREEN:
                endingTime = time.ticks_ms()
                print (endingTime)
                results = (endingTime - startingTime)
                clear()
                break
    #Shows results
    while True: 
        display.set_pen(WHITE)
        display.text(f'Score: {results}ms', 20, 60, 230, 4)
        display.update()

        if button_x.read():
            play()
        elif button_a.read():
            clear()
            main()
    
main()