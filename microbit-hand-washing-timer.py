def showCount(count: number):
    # draw count between 1 and 25 as a spiral
    if count == 1:
        basic.show_leds("""
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    elif count == 2:
        basic.show_leds("""
            # # . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    elif count == 3:
        basic.show_leds("""
            # # # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    elif count == 4:
        basic.show_leds("""
            # # # # .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    elif count == 5:
        basic.show_leds("""
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    elif count == 6:
        basic.show_leds("""
            # # # # #
            . . . . #
            . . . . .
            . . . . .
            . . . . .
            """)
    elif count == 7:
        basic.show_leds("""
            # # # # #
            . . . . #
            . . . . #
            . . . . .
            . . . . .
            """)
    elif count == 8:
        basic.show_leds("""
            # # # # #
            . . . . #
            . . . . #
            . . . . #
            . . . . .
            """)
    elif count == 9:
        basic.show_leds("""
            # # # # #
            . . . . #
            . . . . #
            . . . . #
            . . . . #
            """)
    elif count == 10:
        basic.show_leds("""
            # # # # #
            . . . . #
            . . . . #
            . . . . #
            . . . # #
            """)
    elif count == 11:
        basic.show_leds("""
            # # # # #
            . . . . #
            . . . . #
            . . . . #
            . . # # #
            """)
    elif count == 12:
        basic.show_leds("""
            # # # # #
            . . . . #
            . . . . #
            . . . . #
            . # # # #
            """)
    elif count == 13:
        basic.show_leds("""
            # # # # #
            . . . . #
            . . . . #
            . . . . #
            # # # # #
            """)
    elif count == 14:
        basic.show_leds("""
            # # # # #
            . . . . #
            . . . . #
            # . . . #
            # # # # #
            """)
    elif count == 15:
        basic.show_leds("""
            # # # # #
            . . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
    elif count == 16:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
    elif count == 17:
        basic.show_leds("""
            # # # # #
            # # . . #
            # . . . #
            # . . . #
            # # # # #
            """)
    elif count == 18:
        basic.show_leds("""
            # # # # #
            # # # . #
            # . . . #
            # . . . #
            # # # # #
            """)
    elif count == 19:
        basic.show_leds("""
            # # # # #
            # # # # #
            # . . . #
            # . . . #
            # # # # #
            """)
    elif count == 20:
        basic.show_leds("""
            # # # # #
            # # # # #
            # . . # #
            # . . . #
            # # # # #
            """)
    elif count == 21:
        basic.show_leds("""
            # # # # #
            # # # # #
            # . . # #
            # . . # #
            # # # # #
            """)
    elif count == 22:
        basic.show_leds("""
            # # # # #
            # # # # #
            # . . # #
            # . # # #
            # # # # #
            """)
    elif count == 23:
        basic.show_leds("""
            # # # # #
            # # # # #
            # . . # #
            # # # # #
            # # # # #
            """)
    elif count == 24:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # . # #
            # # # # #
            # # # # #
            """)
    else:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)

def on_sound_loud():
    global do_count, counter
    # (re-)start counting and indicate sound on display
    do_count = 1
    counter = 0
    basic.show_leds("""
        # . . . #
        . . # . .
        . # # # .
        . . # . .
        # . . . #
        """)
    music.play_tone(262, music.beat(BeatFraction.HALF))
input.on_sound(DetectedSound.LOUD, on_sound_loud)

counter = 0
do_count = 0

def on_forever():
    global counter, do_count
    if do_count == 1:
        counter += 1
        showCount(counter)
        if counter >= 25:
            music.play_tone(880, music.beat(BeatFraction.WHOLE))
            do_count = 0
        basic.pause(1200)
    else:
        basic.clear_screen()
basic.forever(on_forever)

