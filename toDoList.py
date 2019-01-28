def main():
    joshuaToDoList()


# Create a task list. A user is presented with the text below.
# Let them select an option to list all of their tasks, add a task to their list, delete a task, or quit the program.
# Make each option a different function in your program.
# Do <strong>NOT</strong> use Google.
# Do <strong>NOT</strong> use other students.
# Try to do this on your own.
# ```
# Congratulations! You're running [YOUR NAME]'s Task List program.
# What would you like to do next?
# 1. List all tasks.
# 2. Add a task to the list.
# 3. Delete a task.
# 0. To quit the program
# ```

toDoList = ["Go to store", "Pick up brother", "Go to lunch with friend", "Go to work"]

def listAllTask():
    for x in toDoList:
        print(x)
#Prints list
def addTask():
    command = input("What would you like to add?")

    toDoList.append(command)
# Adds task to list
def deleteTask():
    command = input("What would you like to delete?")
    toDoList.remove(command)
# Deletes the entered task
def joshuaToDoList():

    command = -1

    while command != 0:
        command = int(input("What would you you like to do?\n 1. List all tasks\n 2. Add a task to the list\n 3. Delete a task\n 0. Quit program"))
        if command == 1:
            listAllTask()
        elif command == 2:
            addTask()
        elif command == 3:
            deleteTask()
        elif command == 0:
            break
        else:
            print("Invalid")

if __name__ == '__main__':
    main()
