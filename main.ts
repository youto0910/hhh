input.onButtonPressed(Button.A, function () {
    if (RESULT == 0) {
        if (PLAYER != 0) {
            led.unplot(PLAYER, 4)
            PLAYER += -1
            led.plot(PLAYER, 4)
            if (led.point(PLAYER, 3)) {
                CATCH += 1
            }
        }
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    RESULT = 1
    basic.showString("YOUR SCORE")
    basic.showNumber(SCORE)
    FAILURE = 0
    LEVEL = 0
    PLAYER = 2
    SCORE = 0
    SUCESS = 0
    RESULT = 0
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    led.plot(PLAYER, 4)
})
input.onButtonPressed(Button.B, function () {
    if (RESULT == 0) {
        if (PLAYER != 4) {
            led.unplot(PLAYER, 4)
            PLAYER += 1
            led.plot(PLAYER, 4)
            if (led.point(PLAYER, 3)) {
                CATCH += 1
            }
        }
    }
})
let BLOCK = 0
let Y = 0
let RESULT = 0
let SUCESS = 0
let SCORE = 0
let PLAYER = 0
let LEVEL = 0
let FAILURE = 0
let CATCH = 0
FAILURE = 0
LEVEL = 0
let LIGHT = 0
PLAYER = 2
SCORE = 0
SUCESS = 0
RESULT = 0
led.plot(PLAYER, 4)
basic.forever(function () {
    if (RESULT == 0) {
        CATCH = 0
        for (let X = 0; X <= 4; X++) {
            Y = 3
            while (Y >= 0) {
                if (led.point(X, Y - 1)) {
                    led.plot(X, Y)
                } else {
                    led.unplot(X, Y)
                }
                Y += -1
            }
        }
        if (LEVEL == 3) {
            BLOCK = randint(0, 5)
            if (BLOCK == 5) {
                BLOCK = randint(0, 3)
                led.plot(BLOCK, 0)
                led.plot(BLOCK + 1, 0)
            } else {
                led.plot(BLOCK, 0)
            }
        } else {
            BLOCK = randint(0, 4)
            led.plot(BLOCK, 0)
        }
        if (led.point(PLAYER, 3)) {
            CATCH += 1
        }
        if (LEVEL == 0) {
            basic.pause(1000)
        } else {
            if (LEVEL == 1) {
                basic.pause(800)
            } else {
                if (LEVEL == 2) {
                    basic.pause(700)
                } else {
                    basic.pause(650)
                }
            }
        }
        LIGHT = 0
        for (let X = 0; X <= 4; X++) {
            if (led.point(X, 3)) {
                LIGHT += 1
            }
        }
        if (CATCH >= LIGHT) {
            SCORE += LEVEL + 1
            SUCESS += 1
            if (SUCESS == 5) {
                SUCESS = 0
                FAILURE = 0
                if (LEVEL == 3) {
                    music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
                } else {
                    LEVEL += 1
                    SCORE += LEVEL * 10
                    music.startMelody(music.builtInMelody(Melodies.Baddy), MelodyOptions.Once)
                }
            } else {
                music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
            }
        } else {
            FAILURE += 1
            if (FAILURE == 2) {
                SUCESS = 0
                FAILURE = 0
                if (LEVEL != 0) {
                    LEVEL += -1
                    SCORE += -5
                    music.startMelody(music.builtInMelody(Melodies.PowerDown), MelodyOptions.Once)
                }
            }
        }
    }
})
