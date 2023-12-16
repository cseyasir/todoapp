#from function import get_todos, write_todos

import function
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now)
while True:
    user_input = input("Type add ,show ,edit ,and complete")
    user_input = user_input.strip()
    if user_input.startswith("add"):
        todo = user_input[4:]
        function.add(todo)
      #  with open("todos.txt", "a") as file:
           # file.write(todo + '\n')

    elif user_input.startswith("show"):
        todos = function.get_todos("todos.txt")


        for index, item in enumerate(todos):
            item= item.strip('\n')
            row= f"{index + 1}-{item}"
            print(row)
    elif user_input.startswith("edit"):
        try:
            number=user_input[4:]
            index=int(number)-1
            todos=function.get_todos("todos.txt")

            new_todo=input("enter the new item")

            todos [index]=new_todo+'\n'
            function.write_todos("todos.txt",todos)
        except ValueError:
            print("your command is not valid.")
            continue
    elif  user_input.startswith("complete"):
        try:
            index=int(user_input[9:])
            todos=function.get_todos("todos.txt")

            number=index-1
            to_remve =todos[number].strip('\n')
            todos.pop(index)
            function.write_todos("todos.txt", todos)
            message=f"todo{to_remve} was removed from list"
        except IndexError or ValueError:
            print("Command not valid.Invalid item to complete")
            continue

    elif "exit" in user_input:
        break
    else:
        print("Commmand is not valid")
print("bye")




