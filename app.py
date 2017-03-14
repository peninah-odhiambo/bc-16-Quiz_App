import json
import os


# Read JSON files from Quizzes folder
root_path = os.path.dirname(os.path.abspath(__file__))
quizzes_path = root_path + '/Quizzes'

def take_quiz(quiz_name):
  with open(quizzes_path + '/' + str(quiz_name) + '.json') as json_data:
    quiz = json.load(json_data)
    return (quiz)


# TODO:
# Import Quizzes quiz import <path_to_quiz_JSON>
# Copy local quiz into quizzes folder and read through it
# Take quiz






