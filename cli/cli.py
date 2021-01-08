def start():
    '''
    Control loop for command-line interface
    '''
    repeat = True
    while repeat:
        command: str = print_prompt()
        result: int = exec_command(command)
        if (result == -1):
            repeat = False

def print_prompt() -> str:
    '''
    Output list of valid commands the user could enter
    '''
    print("Valid commands: q")
    command = input("Enter your command: ")
    return command

def exec_command(command: str) -> int:
    commands = {
        'q': terminate
    }
    result = commands.get(command)() # run function with an empty argument list
    return result

def terminate() -> int:
    '''
    Terminate the program
    '''
    return -1

if __name__ == "__main__":
    start()