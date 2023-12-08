#!/usr/bin/python3
"""
Program called console.py that contains the entry point of the command interpreter
"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter's class HBNBCommand"""

    prompt = '(hbnb) '
    class_mapping = {
        "BaseModel": BaseModel,
        "User": User
    }
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

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        elif line not in self.class_mapping:
            print("** class doesn't exist **")
        else:
            new_model = self.class_mapping[line]()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return  
        if len(args) < 2:
            print("** instance id missing **")
            return
        store_dict = storage.all()
        for key, value in store_dict.items():
            if value.to_dict()['id'] == args[1]:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return  
        if len(args) < 2:
            print("** instance id missing **")
            return
        store_dict = storage.all()
        for key, value in store_dict.items():
            if value.to_dict()['id'] == args[1]:
                del store_dict[key]
                storage.save()
                storage.reload()
                return
        print("** no instance found **")

    def do_all(self, line):
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            lst = []
            store_dict = storage.all()
            for key, value in store_dict.items():
                lst.append(str(value))
            print(lst)

    def do_update(self, line):
        if not line:
            print("** class name missing **")
            return
        args = shlex.split(line)
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return  
        if len(args) < 2:
            print("** instance id missing **")
            return
        store_dict = storage.all()
        for key, value in store_dict.items():
            if value.to_dict()['id'] == args[1]:
                if len(args) < 3:
                    print("** attribute name missing **")
                    return
                if len(args) < 4:
                    print("** value missing **")
                    return
                value.__dict__[args[2]] = args[3]
                value.save()
                return
        print("** no instance found **")
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
