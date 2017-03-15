import json
import os
import shutil


# Read JSON files from Quizzes folder
root_path = os.path.dirname(os.path.abspath(__file__))
quizzes_path = root_path + '/Quizzes'


#Import Quizzes quiz import <path_to_quiz_JSON>
def quiz_import(path_to_quiz_to_import):
    # TO-DO Add error message for json file not found in destination => Quiz not found. Please check source folder.
    # check if file name ends in .json if it doesnt, then it isnt a json file
    # TO-DO: Add error messafe for incorrect path specified

    # Should copy quiz from path to quiz and paste it in /Quizzes folder
    try:
        absolute_path_to_quiz_to_import = os.path.abspath(path_to_quiz_to_import)
        shutil.move(path_to_quiz_to_import, quizzes_path)
        return "I have moved the file"
    except shutil.Error:
        return "I can't move the file. You've probably given me an incorrect path"

def quiz_list():
    #TO-DO: Find out a way of returning both files without the .json 
    quiz_list_array = os.listdir(quizzes_path)
    for file in quiz_list_array:
        if file.endswith(".json"):
            file_name_without_json = file[:-5] # To get rid of .json (slicing method)
            print(file_name_without_json)

# print (quiz_import('C:/Users/andela/Desktop/Imported_Quizzes/food.json'))
# print (quiz_list())

def take_quiz(quiz_name):
    try:
        with open(quizzes_path + '/' + str(quiz_name) + '.json') as json_data:
            quiz_to_take = json.load(json_data)
            #sreturn quiz_to_take
            #print (quiz_to_take)

            for question in quiz_to_take:
                questions_triggered = 0
                score = 0
                while questions_triggered < len(quiz_to_take):
                    print("Please choose an option")
                    print(question["Question"])
                    for key,value in question["choices"].items():
                        print(key, value)
    
                    user_input = input("What is your answer?")
                    if (user_input.capitalize() == question["correctAnswer"]):
                        print("Good job. You've gotten the correct answer!")
                        questions_triggered += 1
                        score +=1
                        print("Your score is", score)
    
                    else:
                        print("Sorry. Wrong answer")
                        print("The correct answer is" + question[" correctAnswer"])
                        questions_triggered +=1
                        score = score
                        print("Your score is", score)



            # for question in quiz_to_take: 
            #     print ("\r\n")
            #     print(question["Question"], ":\r\n", "\r\n".join(question["choices"]))


                # return key + ':\n' + '\n'.join(value)

    except:
        return "Error: Quiz of " + quiz_name + " doesn't exist in local quizzes"
        quiz_to_take = json.load(json_data)
        # return quiz_to_take





print (take_quiz('body'))

    # TO-DO: Identify the quiz to be taken = quiz_name(DONE)
    # TO-DO: Add error message for incorrect quiz_name = Quiz doesn't exist(DONE) 
    # TO-DO: Display one question and its choices of quiz_name ( DONE BUT FIGURE OUT TO BRING ONE AT A TIME)
    # TO-DO: Prompt user for an answer within the choices of the questions displayed (DONE)
    # TO-DO: Check on a functionality for skipping options
    # TO-DO: Program should check whether the answer is correct or incorrect (DONE)
    # TO-DO: Tell user whether the answer is "Correct" or "Incorrect" (DONE)
    # TO-DO: Proceed to the nect questions till the end of the questions. (DONE)
    # TO-DO: Displays the total results in percentage as an integer i.e. full number
    # TO-DO: If 0-29% == You've not done well, 30-50% Average 51-100% Clap for yourself
    # TO-DO: Say Thanks and Prompt user to take another quiz and remind them the command for quizlist
    # TO-DO: Implement timing
    # TO-DO: Fix looping issue = stop it
    # TO-DO: Display right answer when wrong


