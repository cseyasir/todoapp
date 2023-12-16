FILEPATH="todos.txt"
def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local
def write_todos(filepath,todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
def add(todo):
    with open("todos.txt", "a") as file:
        file.write(todo + '\n')
    return todo