function trend (newval: number) {
    if (!(prevval == 0)) {
        olddiff = diffs.shift()
        newdiff = newval - prevval
        diffs.push(newdiff)
        sumd = sumd - olddiff + newdiff
        serial.writeLine(convertToText("" + prevval + " " + ("" + newval) + " " + ("" + newdiff) + " " + ("" + sumd)))
    }
    prevval = newval
    if (Math.abs(sumd) >= SIGNIFICANT) {
        return sumd
    } else {
        return 0
    }
}
let t = 0
let reading = 0
let sumd = 0
let newdiff = 0
let olddiff = 0
let prevval = 0
let SIGNIFICANT = 0
let diffs: number[] = []
diffs = [0, 10]
SIGNIFICANT = 3
let P0_MAX = 812
let CHARGING = images.createImage(`
    . . # # .
    . # . . .
    . # . . .
    . . # # .
    . . . . .
    `)
let DISCHARGING = images.createImage(`
    . # # . .
    . # . # .
    . # . # .
    . # # . .
    . . . . .
    `)
basic.forever(function () {
    reading = pins.analogReadPin(AnalogPin.P0)
    basic.clearScreen()
    t = trend(reading)
    if (t < 0) {
        DISCHARGING.showImage(0)
    }
    if (t > 0) {
        CHARGING.showImage(0)
    }
    basic.pause(1000)
})
