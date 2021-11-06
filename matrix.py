import random
from time import sleep
from colors import *

delay = int(input("please enter the delay in ms: ")) / 1000
number_of_characters = int(input("how many characters do you want: "))
color_input = input("Enter RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN or WHITE for the respective colors: ")

color_output = WHITE

if color_input == "RED":
    color_output = RED
elif color_input == "GREEN":
    color_output = GREEN
elif color_input == "YELLOW":
    color_output = YELLOW
elif color_input == "BLUE":
    color_output = BLUE
elif color_input == "MAGENTA":
    color_output = MAGENTA
elif color_input == "CYAN":
    color_output = CYAN
else:
    color_output = WHITE

while True:
    for i in range(number_of_characters):
        random_number = random.randint(0,1)
        print(f"{color_output}{random_number}", end=" ")
    print()
    sleep(delay)
