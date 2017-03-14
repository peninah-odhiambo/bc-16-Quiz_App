import json
import os
import shutil


# Read JSON files from Quizzes folder
root_path = os.path.dirname(os.path.abspath(__file__))
quizzes_path = root_path + '/Quizzes'


def take_quiz(quiz_name):
  with open(quizzes_path + '/' + str(quiz_name) + '.json') as json_data:
    quiz = json.load(json_data)
    # print('Herereerere')
    # print(os.path.abspath('C:/Users/andela/Desktop/Imported_Quizzes'))
    return (quiz)

# print (take_quiz('body'))

#Import Quizzes quiz import <path_to_quiz_JSON>
def quiz_import(path_to_quiz_to_import):
    # TO:DO Add error message for json file not found in destination => Quiz not found. Please check source folder.
    # check if file name ends in .json if it doesnt, then it isnt a json file
    # TO-DO: Add error messafe for incorrect path specified

    # Should copy quiz from path to quiz and paste it in /Quizzes folder
    try:
        absolute_path_to_quiz_to_import = os.path.abspath(path_to_quiz_to_import)
        shutil.move(path_to_quiz_to_import, quizzes_path)
        return "I have moved the file"
    except shutil.Error:
        return "I can't move the file. You've probably given me an incorrect path"


    


print (quiz_import('C:/Users/andela/Desktop/Imported_Quizzes/food.json'))




# TODO:
# Import Quizzes quiz import <path_to_quiz_JSON>
# Copy local quiz into quizzes folder and read through it
# Take quiz






