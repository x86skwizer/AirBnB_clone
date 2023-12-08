#!/usr/bin/python3
"""
Program called console.py that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """command interpreter's class HBNBCommand"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        pass



    def emptyline(self):
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
