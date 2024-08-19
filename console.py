#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit on EOF."""
        return True

    def emptyline(self):
        """Override emptyline to do nothing."""
        pass

    def do_help(self, arg):
        """Override help to include custom help."""
        super().do_help(arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
