import RPi.GPIO as GPIO
import time
#Declare which GPIO pins are used for LED lights.
gpioGREEN = 22
gpioRED = 23
#Set up GPIO pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(gpioGREEN, GPIO.OUT)
GPIO.setup(gpioRED, GPIO.OUT)

#Introduction quiz and user name input. I would like to improve the introduction by making the user input a string by default.

print("Hello, welcome to this quiz.")
print("There will be a series of multiple choice questions. To answer a question enter the number corresponding to the answer.")
NAME = input("Before we get started what is your name?\n(*please enter your name as a string)\n")
print("Good luck " + NAME + "!")

#Function defined for correct answer and incorrect answer.
#GPIO pins defined. When a question is answered correctly green light flashes, when incorrect red light flashes

def correct_answer():

    print("\nWell done " + NAME + "!")
    a = 0
    while (a < 3):     #While loop. Green light flashes. 
        a = a + 1

        GPIO.setmode(GPIO.BCM)  #I wanted to setup GPIO pins once at the beginning of the code however I had to declare in every function not sure if there is a better way
        GPIO.setup(gpioGREEN, GPIO.OUT)

        GPIO.output(gpioGREEN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(gpioGREEN, GPIO.LOW)
        time.sleep(0.5)

        GPIO.cleanup()
        
        
  def incorrect_answer():

    print("\nUnlucky " + NAME + "!")
    a = 0
    while (a < 3):     #Red light flashes
        a = a + 1

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpioRED, GPIO.OUT)

        GPIO.output(gpioRED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(gpioRED, GPIO.LOW)
        time.sleep(0.5)

        GPIO.cleanup()

#Question printed and answers printed as a list.
#I think the questions could be improved by using dictionaries.


print("\nQuestion 1. When was linux created?")
question_1 = ["1.1988", "2.1990", "3.1993", "4.1991"]
print(question_1[0:4])
answer_1 = input("enter your answer here: ")

#If the answer is correct correct_answer() executed and variable point_1 becomes 1. If incorrect incorrect_answer executed and point_1 becomes 0


if answer_1 == 4:
   correct_answer()
   point_1 = 1
elif answer_1 != 4:
   incorrect_answer()
   point_1 = 0

#The rest of the questions follow the same principle.

print("\nQuestion 2. How would the number 12 be written in binary?")
question_2 = ["1. 010100", "2. 1100", "3. 1011", "4. 0101"]
print(question_2[0:4])
answer_2 = input("enter your answer here: ")

if answer_2 == 2:
   correct_answer()
   point_2 = 1
elif answer_2 != 2:
   incorrect_answer()
   point_2 = 0
answer_1 = input("enter your answer here: ")



print("\nQuestion 3. How many people regularly use the internet? (approximately)")
question_3 = ["1. 7 billion", "2. 4 million", "3. 4 billion", "4. 1 billion"]
print(question_3[0:4])
answer_3 = input("enter your answer here: ")

if answer_3 == 3:
   correct_answer()
   point_3 = 1
elif answer_3 != 3:
   incorrect_answer()
   point_3 = 0
   
print("\nQuestion 4. What does wifi stand for?")
question_4 = ["1.Wireless fidelity", "2.Wizard fingers", "3.Wireless fibres", "4.Wireless fibrillations"]
print(question_4[0:4])
answer_4 = input("enter your answer here: ")

if answer_4 == 1:
   correct_answer()
   point_4 = 1
elif answer_4 != 1:
   incorrect_answer()
   point_4 = 0

print("\nQuestion 5. When was the internet first used to send a message?")
question_5 = ["1.1990", "2.1969", "3.1982", "4.1973"]
print(question_5[0:4])
answer_5 = input("enter your answer here: ")

if answer_5 == 2:
   correct_answer()
   point_5 = 1
elif answer_5!= 2:
   incorrect_answer()
   point_5 = 0

#points from each question added and percentage calculated
#I struggled to get the syntax correct so I did not use the % sign :).

score = point_1 + point_2 + point_3 + point_4 + point_5

print("Congratulations! You have made it to the end of the quiz. You scored:")
print(score , "out of five")
percentage = 100*score/5
print(percentage, "percent")

#Lights flashing at the end of the quiz.
b = 0

while(b < 10):
        b = b + 1

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpioGREEN, GPIO.OUT)

        GPIO.output(gpioGREEN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(gpioGREEN, GPIO.LOW)
        time.sleep(0.5)

        GPIO.cleanup()
