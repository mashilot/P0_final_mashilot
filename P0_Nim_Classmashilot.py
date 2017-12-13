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
#Aaron TA
#David Friend
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import turtle
global number_of_clicks
import random
import sys

#This is code for game of Nim and uses a Nim class and a Egg class in order to play the game.
class Nim():

    def __init__(self):
        """ This method here will create a new nim game

        :param new nim: the integer to be tested
        :return: none """
        global number_of_clicks         #global for number of clicks in event-driven programming
        number_of_clicks = 0
        self.wn = turtle.Screen()
        self.wn.addshape("latest_egg.gif")
        self.wn.onkey(sys.exit, "space")
        self.display_screen()
        self.eggs = 0
        self.egg_list = []
        self.turn = "p"
        self.ask_user_for_eggs()
        self.create_eggs()
        
#The following is a button designed to end the player's turn so that the computer can take a turn.
        self.end_turn_turt = turtle.Turtle()
        self.button_image = "end_button.gif"
        self.wn.register_shape(self.button_image)
        self.end_turn_turt.shape(self.button_image)
        self.end_turn_turt.onclick(self.end_player_turn)
        self.end_turn_turt.penup()
        self.end_turn_turt.setpos(300,280)
        self.end_turn_turt.pendown()

#Textbox instructing the user to enjoy the game.
        self.user_count = turtle.Turtle()
        self.user_count.penup()
        self.user_count.setpos(10,280)
        self.user_count.write("ENJOY THE GAME!!!", align="center", font=("Arial", 20))
        self.wn.update()
        self.user_count.hideturtle()

#Textbox instructing the user how to quit the game early or at the end of the game.
        self.quit_game = turtle.Turtle()
        #self.user_count.write("Enjoy the game", align="center", font=("Arial", 20))
        self.quit_game.penup()
        self.quit_game.setpos(5,-200)
        self.quit_game.write("PRESS SPACEBAR TO QUIT", align="center", font=("Arial", 20))
        self.wn.update()
        self.quit_game.hideturtle()


# The listener should always be last so that all events are performed.
        self.wn.listen()
        self.wn.mainloop()

# End player's turn handler using mouse events
    def end_player_turn(self, x,  y):
        """ This following is a method that is used to end the player's turn once they have decided to pick up 1 to 4 eggs in the bucket

        :param x: mouse event for horizontal mouse event, y: mouse event for vertical mouse event.
        :return: none """

        global number_of_clicks
        if number_of_clicks > 0:        #If statement to end player's turn only once (s)he has picked up eggs greater than zero
            print(number_of_clicks)
            self.computers_turn()

#Computer's turn using modulus division
    def computers_turn(self):
        """ This method that is used to execute the computer's turn once it has decided to pick up 1 to 4 eggs in the bucket using number's divisible by 5

        :param: none
        :return: none """
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

#Method creates egg and multiple eggs that go randomly in the bucket.
    def create_eggs(self):
        for i in range(self.eggs):   # Over here we are simply asking the program to create eggs   
            e = Egg(self, "latest_egg.gif", random.randrange(-100, 120, 4), random.randrange(-100, -90, 4))
            self.egg_list.append(e)

#Method requests the user to input number of eggs they desire for the game.
    def ask_user_for_eggs(self):
        self.eggs = int(input("Pick number of eggs: "))
        while self.eggs < 15:
            self.eggs = int(input("Not enough. Pick number of eggs greater than 15: "))

#This is where the game will display
    def display_screen(self):
        """ This method is going to be the screen that shows the graphical side of the game

        :param: will show the game on this screen
        :return: none """

        self.wn.setup(800,700)              # Determine the window size
        self.wn.title("Game of Nim")        # Window title
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


#Below is our second class 
class Egg:

    def __init__(self, nim, in_img, inx=0, iny=0):     #setting parameters that incorporate an egg
        """ Method that will contain our eggs and navigate where we want to move each during each player's turn, including the computer's turn. 

        :param nim: Nim class, in_img: egg1.gif image, inx and iny: coordinates for eggs
        :return: none """
        self.nim = nim
        self.image = in_img
        self.eggy = turtle.Turtle()
        self.did_click = False
        self.eggy.penup()
        self.eggy.goto(inx, iny)
        self.eggy.shape(self.image)                      #Image of the egg
        self.eggy.onclick(self.egg_motion_left)          #Controls the direction the eggs will be going using mouse events

#Egg's left hand side motion handler
    def egg_motion_left(self,x, y):
        """ This method will move the player's eggs to the left

        :param x: horizontal motion, y: vertical motion
        :return: none """
        if not self.did_click:
            self.did_click = True
            global number_of_clicks

            number_of_clicks += 1
            self.nim.eggs -= 1
            if number_of_clicks == 4:           #Only allows player a maximum of 4 clicks before going to the computer's turn by default
                self.nim.computers_turn()       #Now it is the computer's turn
            self.eggy.setheading(90)
            self.eggy.forward(300)
            self.eggy.left(90)
            self.eggy.forward(280)
            self.eggy.left(90)
            self.eggy.forward(450)

#Egg's right hand side motion handler
    def egg_motion_right(self):             #Egg's motion handler
        """ This method will move the computer's eggs to the right

        :param:none
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

    print ("In this game, you'll enter the number of eggs to play with")
    print ('press the "end" button to call the computers turn')
    print ("press spacebar to quit game")
    print (" ")

    n = Nim()

if __name__ == "__main__":
    main()
