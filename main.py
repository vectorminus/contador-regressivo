x = 10
basic.show_number(x)

def on_every_interval():
    global x
    while x > 0:
        x = x - 1
        basic.show_number(x)
loops.every_interval(1000, on_every_interval)
