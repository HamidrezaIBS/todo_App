'''I try to implement my selection list by using sys module but i got many errors
So i try to itrate my list and make selection with "match case" and it works.
'''

#import sys
import os

print("\n Command Line To Do Application")
print("\n ==============================")

# print(sys.argv[0])

# def print_usage():

select_list = ["-l List all the tasks", "-a Add a new task",
               "-r Remove a task", "-c Complete a task"]

tasks = open("tasks.txt", "r")
append_file = open("tasks.txt", "a")

for value in select_list:
    print(value)

user_input = input("")


def _add(user_input):
    # new_task = input("")
    with open(append_file, "a") as file:
        file.write(f"{user_input}")

def task_list():
    if os.path.exists(tasks):
        with open(tasks) as list_file:
            list_file
            if list_file:
                print(f"\n {list_file}")
            else:
                print("Not todo for today :)")

# def remove_task():

# def completed():    

match(user_input):
    case "-l":
        task_list()
    case "-a":
        _add(input(""))
    case "-r":
        print("remove")
    case "-c":
        print("completed")
    case _:
        print("Invalid select")

# n = len(sys.argv)
# if n == 1:

# print_usage()
