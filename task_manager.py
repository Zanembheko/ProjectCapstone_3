# creating the text file tasks to view tasks and write tasks of the users
# the tasks file is in a readable mode
f = open("tasks.txt", "r")
contents = f.read()
# replaces all the commas and create a new line 
contents = contents.replace(', ', '\n')
f.readlines()
f.close()

# open the file on a writable mode and write all the contents modified above
f = open("tasks.txt", "w")
f.writelines(contents)
f.close()
# open the file and read everything written
f = open("tasks.txt", "r")
contents = f.readlines()
f.close()
# Create an insert method with an index and an element in the contents of the file
# the insert method will check at the position of the element and index it at that position 
contents.insert(0, "Task:\t")
contents.insert(2, "Assigned to:\t")
contents.insert(4, "Task description:\t")
contents.insert(6, "Date assigned:\t")
contents.insert(8, "Due date:\t")
contents.insert(10, "Task complete?\t")
contents.insert(12, "\n")
contents.insert(13, "Assigned to:\t")
contents.insert(15, "Task:\t")
contents.insert(17, "Task description:\t")
contents.insert(19, "Date assigned:\t")
contents.insert(21, "Due date:\t")
contents.insert(23, "Task Complete?\t")

# open the file task on a writable mode and use the .join method to join all elements inserted on the file and then write them to the file.
f = open("tasks.txt", "w")
contents = "".join(contents)
f.write(contents)
f.close()

# create the text file user, to add tasks, view taks, add users and the file can only be managed by the admin
with open("user.txt", "r") as f:
# ask user to enter the username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    username_passw = username + ', ' + password
# for all the contents in the file 
    for line in f:
# if the username and password matches those in the file, then menu should pop up
        if username_passw == line:
            print("Please select one of the following options:")
            print("r - register user\na- add task \nva - view all task \nvm - view my tasks \ne - exit")
            register_user = input()
# if the user chose the register menu, then they should have the credentials for admin, else the user program will discontinue
            if register_user == 'r':
                print("Please note only admin can register new users! ")
# if the user has the admin credentials, then they can add the username and password              
                if username_passw == 'admin, adm1n':
                    f = open("user.txt", "w")
                    new_username = input("Enter the username of the new user: ")
                    new_password = input("Enter the password of the new user: ")
                    new_username_password = new_username + ', ' + new_password
                    f.writelines(new_username_password)
                    f.close()

                else:
                    print("You are not admin therefore you can't register new user!")
                    break;
# if the user chooses add task, then user will have to input the username the task is assigned to and then input the task, description, due date and if the task is complete 
            elif register_user == 'a':
                f = open("tasks.txt", "w")
                task_username = input("enter the username of the person the task is assigned to, the title of the task: ")
                f.writelines(task_username)
                f.write('\n')
                new_task = input("A description of the task and the due date of the task, is the task complete? ")
                f = open("tasks.txt", "r")
                contents = f.read()
# replaces all the commas and create a new line 
                contents = contents.replace(', ', '\n')
                f.readlines()
                f.close()

# open the file on a writable mode and write all the contents modified above
                f = open("tasks.txt", "w")
                f.writelines(contents)
                f.close()
# open the file and read everything written
                f = open("tasks.txt", "r")
                contents = f.readlines()
                f.close()
                contents.insert(0, "Task:\t")
                contents.insert(2, "Assigned to:\t")
                contents.insert(4, "Task description:\t")
                contents.insert(6, "Date assigned:\t")
                contents.insert(8, "Due date:\t")
                contents.insert(10, "Task complete?\t")
                contents.insert(12, "\n")
                contents.insert(13, "Assigned to:\t")
                contents.insert(15, "Task:\t")
                contents.insert(17, "Task description:\t")
                contents.insert(19, "Date assigned:\t")
                contents.insert(21, "Due date:\t")
                contents.insert(23, "Task Complete?\t")

                    # open the file task on a writable mode and use the .join method to join all elements inserted on the file and then write them to the file.
                f = open("tasks.txt", "w")
                contents = "".join(contents)
                f.write(contents)
                f.close()
                #f.writelines(new_task)
               # f.close()
# if user chooses the view all tasks then open the tasks text file for the user to read              
            elif register_user == 'va':
                f = open("tasks.txt", "r")
                f.readlines()
                f.close()
# if user chooses the view my tasks then open the tasks text file for the user to read if his username matches the username in the tasks file else dont open the file
            elif register_user == 'vm':
                your_username = input("Enter your username: ")
                if your_username == task_username:
                    f = open("tasks.txt", "r")
                    f.readlines()
                    f.close
                else:
                    break;
# if the user chooses exit, the break from the code
            elif register_user == 'e':
                break;
        else:
            print("Enter username then comma, a space and then your password:\n")

############################################################        Mr Mentor           ##########################################################
# I was not clear how to deal with the statistics part of the task hopefully I can get the explanation however I believe that is the only part not clear with.

# Regards
# Z Nyhaba
            
            
