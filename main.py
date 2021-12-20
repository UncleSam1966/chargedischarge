def trend(newval: number):
    global olddiff, newdiff, sumd, prevval
    if not (prevval == 0):
        olddiff = diffs.shift()
        newdiff = newval - prevval
        diffs.append(newdiff)
        sumd = sumd - olddiff + newdiff
        serial.write_line(convert_to_text("" + str(prevval) + " " + ("" + str(newval)) + " " + ("" + str(newdiff)) + " " + ("" + str(sumd))))
    prevval = newval
    if abs(sumd) >= SIGNIFICANT:
        return sumd
    else:
        return 0
t = 0
reading = 0
sumd = 0
newdiff = 0
olddiff = 0
prevval = 0
SIGNIFICANT = 0
diffs: List[number] = []
diffs = [0, 10]
SIGNIFICANT = 3
P0_MAX = 812
CHARGING = images.create_image("""
    . . # # .
        . # . . .
        . # . . .
        . . # # .
        . . . . .
""")
DISCHARGING = images.create_image("""
    . # # . .
        . # . # .
        . # . # .
        . # # . .
        . . . . .
""")

def on_forever():
    global reading, t
    reading = pins.analog_read_pin(AnalogPin.P0)
    basic.clear_screen()
    t = trend(reading)
    if t < 0:
        DISCHARGING.show_image(0)
    if t > 0:
        CHARGING.show_image(0)
    basic.pause(1000)
basic.forever(on_forever)
