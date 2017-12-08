import turtle
global number_of_clicks
class Egg:

    def __init__(self, img, inx=0, iny=0):
        self.image = img
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.goto(inx, iny)
        self.t.shape(self.image)
        self.t.onclick(self.move_egg)

    def move_egg(self, x, y):
        global number_of_clicks
        count += 1
        self.t.setheading(90)
        self.t.fd(100)
        self.t.left(90)
        self.t.fd(100)
        self.t.left(90)
        self.t.fd(200)



class Nim:
    global number_of_clicks
    wn = turtle.Screen()
    wn.addshape("egg1.gif")
    e = Egg("egg1.gif")
    e2 = Egg("egg1.gif", 200, 200)

    # game logic
    count = 0
    if count < 4:
        # player turn
        pass
    else:
        # pc turn
        count = 0

    wn.onkey(end_turn, "space")

    wn.mainloop()

    def end_turn(self):
        # pc turn
        pass

def main():
    n = Nim()

main()
