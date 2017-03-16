import json
import sys
import os
import shutil
import time
from termcolor import cprint, colored
from pyfiglet import Figlet,figlet_format
from threading import Thread


root_path = os.path.dirname(os.path.abspath(__file__))
quizzes_path = root_path + '/Quizzes'

time_remaining = 30
def call_take_quiz():
   return take_quiz()

def call_timer():
    global time_remaining
    return timer()


quiz_thread = Thread (target = call_take_quiz) # Calls first function
timer_thread = Thread (target = call_timer) # Calls the second function to run at the same time 

def timer():
    global time_remaining
    print ("Starting countdown ...")
    for i in range (30, 0, -1):
        time.sleep (1)
        time_remaining -= 1
        # print ("Time left is: %s seconds\r")
def quiz_import(path_to_quiz_to_import):
    """Description: Use command to import quiz from external location.
       Usage: quiz_import <path_to_quiz_JSON>
    """
    try:
        absolute_path_to_quiz_to_import = os.path.abspath(path_to_quiz_to_import)
        shutil.copy(path_to_quiz_to_import, quizzes_path)
        return "Quiz successfully copied to local Quizzes folder."
    except shutil.Error:
        return "I can't move the file. Please check file import path. \
                \n Use command quiz_import<path_to_quiz_JSON>"

def quiz_list():
    quiz_list_array = os.listdir(quizzes_path)
    for file in quiz_list_array:
        if file.endswith(".json"):
            file_name_without_json = file[:-5] # To get rid of .json (slicing method)
            print(file_name_without_json)


# def start_quiz(quiz_name):
#     call_quiz_take.start()

def take_quiz(quiz_name):
    global time_remaining
    try:
        with open(quizzes_path + '/' + str(quiz_name) + '.json') as json_data:
            quiz_to_take = json.load(json_data)
            # return quiz_to_take
            # print (quiz_to_take)

            questions_triggered = 0
            score = 0
            
            print ('\n')
            print (colored('-'.center(170,"-"), 'red', attrs=['bold']))

            # start_time = time.time()
            # duration = 5*len(questions)
            # while position < len(questions):
            #     print (question[position])
            #     print (" ")
            #     out_of_time = False

            timer_thread.start()
            while questions_triggered < len(quiz_to_take):
                # print (questions[position])
                # print ("")
                # out_of_time = False
                global time_remaining
                for question in quiz_to_take:
                    print ('\n')
                    print("Please choose an option")
                    print(question["Question"])

                    for key,value in question["choices"].items():
                        print(key + " : " + value)

    
                    user_input = input("What is your answer?") 

                    # elapsed = time.time() - start_time
                    # if elapsed > duration:
                    #     out_of_time = True
                    #     print ("Time up!")
                    #     print (EXIT)

                    if (user_input.capitalize() == question["correctAnswer"]):
                        print("Good job. You've gotten the correct answer!")
                        questions_triggered += 1
                        score +=1
                        print("Your score is", score)
                        
    
                    else:
                        print("Sorry. Wrong answer")
                        print("The correct answer is " + question["correctAnswer"])
                        questions_triggered +=1
                        score = score
                        print("Your score is", score)

                    print ("You scored", score, "out of", questions_triggered)
                    if time_remaining < 1:
                        print ("Timeout")
                        return 
                        
                    else:
                        print ("Time reamining:" + str(time_remaining) + "s") 
                        


                print ('\n') 

                percentage = score/questions_triggered * 100
                percentage = int(round(percentage))
                print("Total Score percentage is {} %".format(percentage))  

                print ('\n')

                print (colored('-'.center(170,"-"), 'green', attrs=['bold']))

                
            print ('\n')

             

        # def countdown (count):
        #     while (count >= 0):
        #         print ("The count is : ", count)
        #         count -= 10
        #         time.sleep (1)

        # countdown (30)
        # print ("Time Up!")

                    # break 


    except Exception as e:
        return "Error: Quiz of " + quiz_name + " doesn't exist in local quizzes" + e
        quiz_to_take = json.load(json_data)
        # return quiz_to_take

    # TO-DO: Identify the quiz to be taken = quiz_name(DONE)
    # TO-DO: Add error message for incorrect quiz_name = Quiz doesn't exist(DONE) 
    # TO-DO: Display one question and its choices of quiz_name ( DONE)
    # TO-DO: Prompt user for an answer within the choices of the questions displayed (DONE)
    # TO-DO: Check on a functionality for skipping options
    # TO-DO: Program should check whether the answer is correct or incorrect (DONE)
    # TO-DO: Tell user whether the answer is "Correct" or "Incorrect" (DONE)
    # TO-DO: Proceed to the nect questions till the end of the questions. (DONE)
    # TO-DO: Displays the total results in percentage as an integer i.e. full number(DONE)
    # TO-DO: If 0-29% == You've not done well, 30-50% Average 51-100% Clap for yourself
    # TO-DO: Say Thanks and Prompt user to take another quiz and remind them the command for quizlist(DONE)
    # TO-DO: Implement timing
    # TO-DO: Fix looping issue = stop it (DONE)
    # TO-DO: Display right answer when wrong (DONE)



