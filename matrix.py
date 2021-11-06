import random
from time import sleep

delay = int(input("please enter the delay in ms: ")) / 1000
number_of_characters = int(input("how many characters do you want: "))

while True:
    for i in range(number_of_characters):
        random_number = random.randint(0,1)
        print(random_number, end=" ")
    print()
    sleep(delay)
