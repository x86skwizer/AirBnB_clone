#!/usr/bin/python3
"""
Program called console.py that contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter's class HBNBCommand"""
    prompt = '(hbnb) ' 
    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print (f"hi, {person}")
        else:
            print ("hi")
    
    def do_EOF(self, line):
        return True
    
    def postloop(self):
        print

if __name__ == '__main__':
    HBNBCommand().cmdloop()
