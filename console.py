#!/usr/bin/python3
"""
Program called console.py that contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter's class HBNBCommand"""
    pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
