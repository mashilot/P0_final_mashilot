######################################################################
# Author: Siso Mashilo
# Username: mashilot
#
# Assignment: P0: Nim Class
#Purpose: Practice breaking a larger problem down into smaller "mental chunks" using functions
#Gain practice using loops and modulus (%)
#
######################################################################
# Acknowledgements:
# Original Author: Dr. Jan Pearce
#Dr. Scott Heggen
# Alex Guis
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import time
import turtle
global number_of_clicks
import random

class Nim():

    def __init__(self):
        """ This method here will create a new nim game

        :param new nim: the integer to be tested
        :return: none """
        global number_of_clicks
        number_of_clicks = 0
        self.wn = turtle.Screen()
        self.wn.addshape("new_egg.gif")
        #self.wn.onkey(self.end_my_turn, "space")
        self.display_screen()
        self.eggs = 0
        self.egg_list = []
        self.turn = "p"
        self.ask_user_for_eggs()
        self.create_eggs()


        # Be last
        self.wn.listen()
        self.wn.mainloop()

    def computers_turn(self):
        print("Computer's turn")
        for i in range(4, 0, -1):
            if self.eggs % i == 0:
                for j in range(i):
                    count = 0
                    for egg in self.egg_list:
                        if count <= i:
                            if not egg.did_click:
                                egg.did_click = True
                                egg.egg_motion_right()
                                count += 1
                                print(self.eggs)

                break



    def create_eggs(self):
        for i in range(self.eggs):
            e = Egg(self, "new_egg.gif", random.randrange(-100, 120, 4), random.randrange(-100, -90, 4))
            self.egg_list.append(e)

    def ask_user_for_eggs(self):
        self.eggs = int(input("Pick number of eggs: "))
        while self.eggs < 15:
            self.eggs = int(input("Not enough. Pick number of eggs greater than 15: "))


    def display_screen(self):
        """ This method is going to be the screen that shows the graphical side of the game

        :param: will show the game on this screen
        :return: none """


        self.wn.setup(800,700)              # Determine the window size
        self.wn.title("Game of Nim")        # Change the window title
        self.wn.bgcolor("red")              # Set the background color
        bucket = turtle.Turtle()            # Create our favorite turtle

        bucket.hideturtle()
        bucket.pensize(5)
        bucket.penup()
        bucket.goto(-150, -150)
        bucket.pendown()
        bucket.forward(300)
        bucket.left(90)
        bucket.forward(300)
        bucket.penup()
        bucket.goto(-150, -150)
        bucket.pendown()
        bucket.forward(300)



class Egg:

    def __init__(self, nim, in_img, inx=0, iny=0):            #setting parameters that incorporate an egg
        self.nim = nim
        self.image = in_img
        self.eggy = turtle.Turtle()
        self.did_click = False
        self.eggy.penup()
        self.eggy.goto(inx, iny)
        self.eggy.shape(self.image)
        self.eggy.onclick(self.egg_motion)

    def egg_feature(self):
        """ This method here will create a new nim game

    :param new nim: the integer to be tested
    :return: none """

    # wn = turtle.Screen()
    # wn.addshape("new_egg.gif")
    # eggy = ("new_egg.gif")
    # eggy2 =("new_egg.gif", 60, 200)

    def egg_motion(self, x, y):
        """ This method will move the player's eggs to the left

        :param new nim: the integer to be tested
        :return: none """
        if not self.did_click:
            self.did_click = True
            global number_of_clicks
            self.eggy.setheading(90)
            self.eggy.forward(300)
            self.eggy.left(90)
            self.eggy.forward(280)
            self.eggy.left(90)
            self.eggy.forward(450)
            number_of_clicks += 1
            self.nim.eggs -= 1
            if number_of_clicks >= 4:
                self.nim.computers_turn()

    def egg_motion_right(self):
        """ This method will move the computer's eggs to the right

        :param new nim:
        :return: none """

        self.eggy.setheading(90)
        self.eggy.forward(300)
        self.eggy.right(90)
        self.eggy.forward(280)
        self.eggy.right(90)
        self.eggy.forward(450)
        global number_of_clicks
        number_of_clicks = 0
        self.nim.eggs -= 1

def main():

    n = Nim()

   # winner = create_eggs()
    #while winner > 0:
     #   winner = ask_user_for_eggs(winner)
      #  print(winner)
       # winner = computers_turn(winner)
        #print(winner)

        #n.players_turns()


if __name__ == "__main__":
    main()
