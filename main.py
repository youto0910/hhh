def on_button_pressed_a():
    global PLAYER, CATCH
    if RESULT == 0:
        if PLAYER != 0:
            led.unplot(PLAYER, 4)
            PLAYER += -1
            led.plot(PLAYER, 4)
            if led.point(PLAYER, 3):
                CATCH += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global RESULT, FAILURE, LEVEL, PLAYER, SCORE, SUCESS
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    RESULT = 1
    basic.show_string("YOUR SCORE")
    basic.show_number(SCORE)
    FAILURE = 0
    LEVEL = 0
    PLAYER = 2
    SCORE = 0
    SUCESS = 0
    RESULT = 0
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    led.plot(PLAYER, 4)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global PLAYER, CATCH
    if RESULT == 0:
        if PLAYER != 4:
            led.unplot(PLAYER, 4)
            PLAYER += 1
            led.plot(PLAYER, 4)
            if led.point(PLAYER, 3):
                CATCH += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

BLOCK = 0
Y = 0
RESULT = 0
SUCESS = 0
SCORE = 0
PLAYER = 0
LEVEL = 0
FAILURE = 0
CATCH = 0
FAILURE = 0
LEVEL = 0
LIGHT = 0
PLAYER = 2
SCORE = 0
SUCESS = 0
RESULT = 0
led.plot(PLAYER, 4)

def on_forever():
    global CATCH, Y, BLOCK, LIGHT, SCORE, SUCESS, FAILURE, LEVEL
    if RESULT == 0:
        CATCH = 0
        for X in range(5):
            Y = 3
            while Y >= 0:
                if led.point(X, Y - 1):
                    led.plot(X, Y)
                else:
                    led.unplot(X, Y)
                Y += -1
        if LEVEL == 3:
            BLOCK = randint(0, 5)
            if BLOCK == 5:
                BLOCK = randint(0, 3)
                led.plot(BLOCK, 0)
                led.plot(BLOCK + 1, 0)
            else:
                led.plot(BLOCK, 0)
        else:
            BLOCK = randint(0, 4)
            led.plot(BLOCK, 0)
        if led.point(PLAYER, 3):
            CATCH += 1
        if LEVEL == 0:
            basic.pause(1000)
        else:
            if LEVEL == 1:
                basic.pause(800)
            else:
                if LEVEL == 2:
                    basic.pause(700)
                else:
                    basic.pause(650)
        LIGHT = 0
        for X2 in range(5):
            if led.point(X2, 3):
                LIGHT += 1
        if CATCH >= LIGHT:
            SCORE += LEVEL + 1
            SUCESS += 1
            if SUCESS == 5:
                SUCESS = 0
                FAILURE = 0
                if LEVEL == 3:
                    music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
                else:
                    LEVEL += 1
                    SCORE += LEVEL * 10
                    music.start_melody(music.built_in_melody(Melodies.BADDY), MelodyOptions.ONCE)
            else:
                music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
        else:
            FAILURE += 1
            if FAILURE == 2:
                SUCESS = 0
                FAILURE = 0
                if LEVEL != 0:
                    LEVEL += -1
                    SCORE += -5
                    music.start_melody(music.built_in_melody(Melodies.POWER_DOWN),
                        MelodyOptions.ONCE)
basic.forever(on_forever)
