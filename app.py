import click
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


def call_timer():
    global time_remaining
    return timer()



timer_thread = Thread (target = call_timer) # Calls the second function to run at the same time 

def timer():
    global time_remaining
    print ("Starting countdown ...")
    for i in range (30, 0, -1):
        time.sleep (1)
        time_remaining -= 1
       
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

                   
                    if (user_input.capitalize() == question["correctAnswer"]):
                        click.secho("Good job. You've gotten the correct answer!", fg = 'green')
                        questions_triggered += 1
                        score +=1
                        print("Your score is", score)
                        
    
                    else:
                        click.secho("Sorry. Wrong answer", fg = 'red')
                        click.secho("The correct answer is " + question["correctAnswer"], fg = 'cyan')
                        questions_triggered +=1
                        score = score
                        print("Your score is", score)

                    print ("You scored", score, "out of", questions_triggered)
                    if time_remaining < 1:
                        click.secho("Timeout!!!!", bold = True)
                        return 

                    else:
                        print ("Time reamining:" + str(time_remaining) + "s") 
                        


                print ('\n') 
                """Displays the total results in percentage as an integer i.e. full number(DONE)
                """

                percentage = score/questions_triggered * 100
                percentage = int(round(percentage))
                click.secho ("TOTAL SCORE PERCENTAGE IS {} %".format(percentage), bold = True)  

                print ('\n')

                print (colored('-'.center(170,"-"), 'green', attrs=['bold']))

                
            print ('\n')

             
    except Exception as e:
        return "Error: Quiz of " + quiz_name + " doesn't exist in local quizzes" 
        quiz_to_take = json.load(json_data)
        # return quiz_to_take



    # TO-DO: Say Thanks and Prompt user to take another quiz and remind them the command for quizlist(DONE)




