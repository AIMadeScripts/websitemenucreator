#!/usr/bin/env python

###===Import Modules Go Here===###
import os

###===Setting your variables to blank values===###
target = ""
target2 = ""

###===Separator Function For Pretty Menu===###
def print_separator():
    print("=" * 50)

###===Your Viewable Menu===###
def menu():
    clear_screen()
    print('Scanner Script!')
    variable_counts = {}
    print('Your script has some variables $target, $target2')
    print_separator()
    print('1. Nmap')
    print('2. Ping')
    variable_counts = {}
    print(f'set_target | current variable target = {target}')
    print(f'set_target2 | current variable target2 = {target2}')
    print('(exit) Exit')

###===Making Clear Screen Work On Windows And Linux===###
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

###===When You Choose An Option It Runs One Of These===###
def nmap():
    print('You selected nmap')
    nmap = f"nmap -sV -sC {target}"
    try:
        os.system(nmap)
    except KeyboardInterrupt:
        print('nmap interrupted by user')
    input('Press enter to return to menu...')

def ping():
    print('You selected ping')
    ping = f"ping {target2}"
    try:
        os.system(ping)
    except KeyboardInterrupt:
        print('ping interrupted by user')
    input('Press enter to return to menu...')

def set_target():
    global target
    target = input('Enter a new target:')
    input('Press enter to return to menu...')

def set_target2():
    global target2
    target2 = input('Enter a new target:')
    input('Press enter to return to menu...')

def exit_menu():
    print('Goodbye!')
    exit()

###===Enter Your Choice And Then It Will Activate That Option===###
if __name__ == '__main__':
    while True:
        menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            nmap()
        if choice == '2':
            ping()
        if choice == 'set_target':
            set_target()
        if choice == 'set_target2':
            set_target2()
        elif choice.lower() == 'exit':
            exit_menu()
        else:
            print('Invalid choice. Try again.')
