#!/usr/bin/python3
import cmd, shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit on EOF."""
        return True

    def do_help(self, arg):
        """Override help to include custom help."""
        super().do_help(arg)
        
    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it and prints the id."""
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)
            
    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id."""
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

    def emptyline(self):
        """Override emptyline to do nothing."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
