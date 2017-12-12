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
#Will TA
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import turtle
global number_of_clicks
import random
import sys

#This is code for game of Nim and uses a Nim class and a Egg class in order to play the game
class Nim():

    def __init__(self):
        """ This method here will create a new nim game

        :param new nim: the integer to be tested
        :return: none """
        global number_of_clicks
        number_of_clicks = 0
        self.wn = turtle.Screen()
        self.wn.addshape("new_egg.gif")
        self.wn.onkey(sys.exit, "space")
        self.display_screen()
        self.eggs = 0
        self.egg_list = []
        self.turn = "p"
        self.ask_user_for_eggs()
        self.create_eggs()
        self.end_turn_turt = turtle.Turtle()
        self.button_image = "button_end.gif"
        self.wn.register_shape(self.button_image)
        self.end_turn_turt.shape(self.button_image)
        self.end_turn_turt.onclick(self.end_player_turn)
        #self.end_turn_turt. (x=200, y=200)

       # self.sys.pos(200, 200)

         # Be last
        self.wn.listen()
        self.wn.mainloop()

    def end_player_turn(self, x,  y):
        global number_of_clicks
        if number_of_clicks > 0:
            print(number_of_clicks)
            self.computers_turn()




    def computers_turn(self):
        print("Computer's turn")
        comps_num = 0
        comps_go = self.eggs
        if (comps_go -4) % 5 == 0:
            comps_go -= 4
            comps_num = 4
            print("Computer has taken 4")
        elif (comps_go -3) % 5 == 0:
            comps_go -= 3
            comps_num = 3
            print("Computer has taken 3")
        elif(comps_go - 2) % 5 == 0:
            comps_go -= 2
            comps_num = 2
            print("Computer has taken 2")
        else:
            comps_go -= 1
            comps_num = 1
            print("Computer has taken 1")
        if comps_go == 0:
            print("Computer wins")
            exit()
        print(comps_go)
        for egg in self.egg_list:
            if comps_num == 0:
                break
            else:
                if not egg.did_click:
                    egg.did_click = True
                    egg.egg_motion_right()
                    comps_num -= 1

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

      # Turtle draws the bucket that the eggs go in for the game
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

    def egg_motion(self,x, y):
        """ This method will move the player's eggs to the left

        :param new nim: the integer to be tested
        :return: none """
        if not self.did_click:
            self.did_click = True
            global number_of_clicks

            number_of_clicks += 1
            self.nim.eggs -= 1
            if number_of_clicks == 4:
                self.nim.computers_turn()
            self.eggy.setheading(90)
            self.eggy.forward(300)
            self.eggy.left(90)
            self.eggy.forward(280)
            self.eggy.left(90)
            self.eggy.forward(450)

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

if __name__ == "__main__":
    main()
