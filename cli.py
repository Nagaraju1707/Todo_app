# from Functions import get_todos, write_todos
import Functions
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now) 
while True:

    user_action = input("Enter add,show,edit,complete or exit: ")
    user_action = user_action.strip()

    if  user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = Functions.get_todos()
        todos.append(todo)
        Functions.write_todos(todos)

    elif  user_action.startswith('show'):

        todos = Functions.get_todos()
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}:{item}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number -1
            todos = Functions.get_todos()
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + '\n'
            Functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = Functions.get_todos()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            Functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list. "
            print(message)
        except IndexError:
            print("There is no item with that number.")
    elif user_action.startswith('exit'):
        break
    else:
        print("command is not valid.")
print(" bye!chilla have a good day.")





