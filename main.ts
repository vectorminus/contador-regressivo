let x = 30
basic.showNumber(x)
loops.everyInterval(1000, function () {
    while (x > 0) {
        x = x - 1
        basic.showNumber(x)
    }
})
