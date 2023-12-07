#!/usr/bin/python3
"""
Program called console.py that contains the entry point of the command interpreter
"""
import cmd


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

    def emptyline(self):
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
