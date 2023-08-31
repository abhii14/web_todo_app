FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    """read a text file and return the string to todo fn"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """write the todo item list in txt files"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
