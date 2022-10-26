import turtle
import time
from random import randint, shuffle
import math


def dotted_line(t, division, start, end, inverted_color=False):
    """Module to draw 'dotted' line from two points in xy space."""
    if inverted_color:
        b_w = ["white", "grey"]
    else:
        b_w = ["grey", "white"]
    t.penup()
    t.pensize(4)
    t.goto(start)

    # Distance from 2 points in xy space
    d_xy = math.sqrt(math.pow((start[0] - end[0]), 2) + math.pow((start[1] - end[1]), 2))
    dot_length = d_xy / division

    # Getting the angle
    alpha = math.degrees(math.acos(abs(start[0] - end[0]) / d_xy))
    t.left(alpha)
    for i in range(division):
        t.pendown()
        t.color(b_w[i % 2])
        t.forward(dot_length)
    t.penup()
    t.goto(start)
    t.seth(0)


class Race:
    def __init__(self):
        # Useful variables
        self.colors = ["cyan", "darkorange", "hotpink", "darkred", "springgreen", "lightsalmon"]
        self.winner = ''
        self.game_running = True
        self.goal = 224

        # Screen init
        self.screen = turtle.Screen()
        self.screen.title("Turtle Racing Game")
        self.screen.setup(500, 400)
        self.screen.bgcolor("black")

        # Turtles created to draw things
        self.win_turtle = turtle.Turtle()
        self.goal_turtle = turtle.Turtle()
        self.goal_turtle.speed("fastest")
        self.goal_turtle.hideturtle()
        dotted_line(self.goal_turtle, 7, (self.goal, -140), (self.goal, 140))
        dotted_line(self.goal_turtle, 7, (self.goal+4, -140), (self.goal+4, 140), True)

        # Creating turtles
        self.turtle_lst = [turtle.Turtle(shape="turtle") for _ in self.colors]

        # Asking for bet input
        self.user_bet = self.screen.textinput(title="Make your bet", prompt=(f'Which turtle will win...\n'
                                                                             f'{self.colors}').lower())
        # Starting the game.
        self.turtle_start()
        self.screen.exitonclick()

    def turtle_start(self):
        """
        Setting turtles position.
        Every other core function is called inside.
        1. shuffling turtles to not have always the same color on top
        2. setting starting coord.
        3. looping on turtle_lst and moving the turtle obj inside to the correct pos.
        4. calling self.title()
        5. calling self.race_instance()
        6. printing self.bet_checking()
        Return None
        """
        shuffle(self.colors)
        x, y = -240, 100
        for i, n in enumerate(self.turtle_lst):
            n.color(self.colors[i])
            n.penup()
            n.goto(x, y)
            y -= 40
        self.title()
        self.race_instance()
        print(self.bet_checking())

    def race_instance(self):
        """
        Turtle movement function.
        1. Moving randomly one for one using for loop
        2. if one surpass the goal, the loop closes.
        3. Taking the attribute color to determine the winner
        4. the winner rotates for joy!
        """
        while self.game_running:
            for n in self.turtle_lst:
                n.forward(randint(0, 10))
                if n.xcor() > self.goal:
                    self.game_running = False
                    self.winner = n.pencolor()
                    n.left(720)

    def bet_checking(self):
        """
        Compare winner with bet.
        return str
        """
        self.win_turtle.clear()
        if self.user_bet in self.colors:
            if self.winner.lower() == self.user_bet.lower():
                self.win_turtle.write(f"{self.winner.capitalize()} turtle won,\nYou won the bet.", move=False, align="left",
                                      font=("Arial", 13, "bold"))
                return f"{self.winner.capitalize()} won, and you won the bet."
            else:
                self.win_turtle.write(f"{self.winner.capitalize()} turtle won,\nYou lost the bet.", move=False, align="left",
                                      font=("Arial", 13, "bold"))
                return f"{self.winner.capitalize()} won, and you lost the bet."
        else:
            self.win_turtle.write(f"{self.winner.capitalize()} turtle won", move=False, align="left",
                                  font=("Arial", 13, "bold"))
            return f"Invalid bet, wtf...you wrote {self.user_bet}"

    def title(self):
        """
        Draw some text on the upper side of the screen.
        """
        self.win_turtle.hideturtle()
        self.win_turtle.penup()
        self.win_turtle.goto(-70, 150)
        self.win_turtle.pensize(3)
        self.win_turtle.color("white")
        time.sleep(1)
        self.win_turtle.write("Ready...", move=False, align="left", font=("Arial", 14, "normal"))
        time.sleep(1)
        self.win_turtle.clear()
        self.win_turtle.write("...Set...", move=False, align="left", font=("Arial", 14, "normal"))
        time.sleep(1)
        self.win_turtle.clear()
        self.win_turtle.write("...GOOOO! :D", move=False, align="left", font=("Arial", 14, "normal"))


race = Race()

