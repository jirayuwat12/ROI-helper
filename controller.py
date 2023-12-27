import sys

class Controller:
    def __init__(self):
        self.COMMAND_DIC = {
            "help": self.help,
            "exit": self.exit
        }

    def run(self):
        while True:
            command, args = self.get_command()
            if command in self.COMMAND_DIC:
                self.COMMAND_DIC[command](*args)
            else:
                print("Command not found. Type 'help' for available commands")


    def get_command(self):
        buffer = input(">>> ")
        command, *args = buffer.split(" ")
        
        return command.lower(), args
    
    def help(self):
        print("Available commands:")
        for command in self.COMMAND_DIC.keys():
            print(command)
    
    def exit(self):
        sys.exit(0)
