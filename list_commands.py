# """

# import sys
# import cmd
# from docopt import docopt, DocoptExit
# import my_methods


#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    Quiz_app list_quizzes
    Quiz_app quiz_import <quiz_path> 
    Quiz_app take_quiz <quiz_name>
    Quiz_app add total score
    Quiz_app add timer
    Quiz_app (-i | --interactive)
    Quiz_app (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
import time
import clint
from clint.textui import colored
from colorama import init 
from colorama import Fore, Back, Style
from docopt import docopt, DocoptExit
from pyfiglet import Figlet,figlet_format
from termcolor import cprint, colored
from app import quiz_import
from app import quiz_list
from app import take_quiz




def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


# class MyInteractive(cmd.Cmd):

#     print (colored('='.center(170,"="), 'green', attrs=['bold']))
#     print (colored('='.center(170,"="), 'green', attrs=['bold']))
#     cprint(figlet_format('SMART', font='univers'),'red', 'on_grey', attrs=['bold'])
#     print (colored('='.center(170,"="), 'green', attrs=['bold']))
#     print (colored('='.center(170,"="), 'green', attrs=['bold']))
#     print ("\n")
#     cprint(figlet_format('READY?'), 'yellow', attrs=['bold'])
#     intro = "Let's get started!\n" + "(type help for a command list.)"
#     prompt = '(quiz_list) '

    
#     print("-".center(73,"-"))


#     file = None
class MyInteractive(cmd.Cmd):
    print (colored('='.center(170,"="), 'green', attrs=['bold']))
    print (colored('='.center(170,"="), 'green', attrs=['bold']))
    f = Figlet(font = 'slant')
    cprint(figlet_format('SMART', font='univers'),'red', 'on_grey', attrs=['bold'])
    print (colored('='.center(170,"="), 'green', attrs=['bold']))
    print (colored('='.center(170,"="), 'green', attrs=['bold']))
    cprint(figlet_format('READY?'), 'yellow', attrs=['bold'])
    intro = "Let's get started!\n" + "(type help for a command list.)"
    prompt = '(quiz_list) '
    file = None

#definition of docopt commands
    @docopt_cmd
    def do_list_quizzes(self, args):
        """Usage: list_quizzes"""
        quiz_list()

    @docopt_cmd
    def do_quiz_import(self, args):
        """Usage: quiz_import <quiz_path> """
        quiz_import(args["<quiz_path>"])

    @docopt_cmd
    def do_take_quiz(self, args):
        """Usage: take_quiz <quiz_name> """
        print(take_quiz(args["<quiz_name>"]))
        

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print (colored('='.center(170,"="), 'green', attrs=['bold']))
        print (colored('='.center(170,"="), 'green', attrs=['bold']))
        print('Thank you for trying out the quizzes!\n')
        print("Try another quiz!\n")
        print (colored('='.center(170,"="), 'green', attrs=['bold']))
        print (colored('='.center(170,"="), 'green', attrs=['bold']))
        cprint(figlet_format("Visit Soon!"), 'yellow', attrs=['bold'])
        
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        MyInteractive().cmdloop()
    except KeyboardInterrupt:
        exit()

print(opt)