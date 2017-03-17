SMART 

The aim of this project is to create Command Line quiz application written in Python Language.  The app in question is named SMART.

Features
	a) Contains the lists of all the available quizzes from the terminal
	b) Allows the user to import quizzes from external sources(.json files only).
	c) Shows the user the list of questions in every quiz as well as different answer options.
	d) Allows the user to choose the preffered answers from the choices provided.
	e) Shows the user results depending on their choices after each question and the accumulated results.
	f) The app will have a countdown timer.

Requirements

appdirs==1.4.3
args==0.1.0
click==6.7
clint==0.5.1
colorama==0.3.7
docopt==0.6.2
easy-timer==0.0.4
Jinja2==2.9.5
MarkupSafe==1.0
mog-commons==0.2.2
packaging==16.8
pyfiglet==0.7.5
pyparsing==2.2.0
six==1.10.0
termcolor==1.1.0


[Python 2.7.11] (https://www.python.org/downloads/) : Python Interpreter

[Colorama==0.3.7 ] (https://pypi.python.org/pypi/colorama) : Colour and font enhancing for python applications. pip install colorama

[pyfiglet==0.7.5] (https://pypi.python.org/pypi/pyfiglet): Takes ASCII text and renders it in ASCII art fonts. pip install https://pypi.python.org/packages/source/p/pyfiglet/pyfiglet-0.7.5.tar.gz

[termcolor==1.1.0] (https://pypi.python.org/pypi/termcolor): ANSII Color formatting for output in terminal. pip install termcolor

To install all requirements, download the [requirements.txt] (https://github.com/peninah-odhiambo/bc-16-Quiz_App/blob/master/requirements.txt) file then type this in your terminal application:

         
         pip install -r /path/to/requirements.txt

To get you started, after installation, use the commands, listonline and download quiz or copy the quizzes in [this] (https://github.com/peninah-odhiambo/bc-16-Quiz_App/tree/master/Quizzes) project's github repository and use the importquiz command to import them into the Quizzler library.
Commands

Command	Description
help	Displays all available commands and their descriptions
help (command)	Describes the command
listquizzes	Displays available local quizzes
takequiz (quiz name)	Launches the local quiz quiz name
listonline	Display available online quizzes
download (quiz)	Add a quiz to the local collection from online source
upload (quiz source path	Add quiz to online collection
importquiz (quiz source path)	Add quiz to local collection from external source
Copyright and Licensing


Contact Information

Find the author at [peninah-odhiambo] (https://github.com/peninah-odhiambo) on github. -->