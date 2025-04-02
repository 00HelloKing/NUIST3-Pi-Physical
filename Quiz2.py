# Author: Jin Kaifeng
# Date: 2/4/2025

import RPi.GPIO as GPIO
import time

#  red and green
GPIO.setmode(GPIO.BCM)
RED_PIN = 18
GREEN_PIN = 17  

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.output(RED_PIN, GPIO.LOW)
GPIO.output(GREEN_PIN, GPIO.LOW)


def quiz():
    print("\nPython Test")
    print("Please answer with option letters:")

    # questions and answers
    questions = [
        "1) Which of the following is NOT a python data type?\na) int\nb) float\nc) rational\nd) string\ne) boot",
        "2) Which of the following is NOT a built-in operation in Python?\na) +\nb) %\nc) abs()\nd) sqrt()",
        "3) In a mixed-type expression involving its and floats, Python will convert？\na) floats to ints\nb) ints to strings\nc) floats and ints to string\nd) ints to floats",
        "4) The best structure for implementing a multi-way decision in Python is？\na) if\nb) if-else\nc) if-elif-else\nd) try",
        "5) What statement can be executed in the body of a loop to cause it to terminate?\na) if\nb) exit\nc) continue\nd) break"

    ]

    answers = [ "c", 
		"d", 
		"d", 
		"c", 
		"d"]

    score = 0



    try:
        # traversal
        for idx, question in enumerate(questions):
            print(f"\n{question}")
            user_answer = input("PLease enter your answers: ").strip().lower()

            # check answers and control the LED
            if user_answer == answers[idx]:
                GPIO.output(GREEN_PIN, GPIO.HIGH)
                print("Correct!")
                score += 1
            else:
                GPIO.output(RED_PIN, GPIO.HIGH)
                print("Incorrect!")                
           # time.sleep(0.5)         
           # GPIO.output(GREEN_PIN, GPIO.LOW)
           # GPIO.output(RED_PIN, GPIO.LOW)
           # time.sleep(0.5)       

            time.sleep(1)          
            GPIO.output(GREEN_PIN, GPIO.LOW)
            GPIO.output(RED_PIN, GPIO.LOW)
            time.sleep(0.5)        

        # final score
        print(f"\nQuiz finished! Correct rate: {score}/5")


    finally:
        GPIO.cleanup()  # clear


if __name__ == "__main__":
    quiz()
