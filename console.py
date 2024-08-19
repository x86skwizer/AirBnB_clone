#!/usr/bin/python3
"""
Program called console.py that contains
the entry point of the command interpreter
"""
import cmd, shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models import storage
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """command interpreter's class HBNBCommand"""

    prompt = '(hbnb) '
    class_mapping = {
        "BaseModel": BaseModel,
        "User": User,
        'State': State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def default(self, line):
        """handle Class name input
        """
        class_mapping = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        args = line.strip()
        args = args.split(".")
        if len(args) != 2:
            cmd.Cmd.default(self, line)
            return
        name_class = args[0]
        if '(' in args[1]:
            arg_parts = args[1].split('(')
            command_parts = arg_parts[1].split(')')
            command_p = command_parts[0].split(',')
            str_com = " ".join(str(e) for e in command_p)
            if len(command_parts) > 1:
                command = [arg_parts[0], args[0], command_parts[0]]
                if command[0] in class_mapping.keys():
                    call = "{} {}".format(args[0], str_com)
                    return class_mapping[command[0]](call)
        print("*** Unknown syntax: {}".format(line))

    def do_count(self, line):
        """Count instanes of a class:
        Usage: <class name>.count().
        """
        if not line:
            print("** class name missing **")
            return
        args = shlex.split(line)
        if args[0] not in self.class_mapping:
            print("** class doesn't exist **")
            return
        store_dict = storage.all()
        n = 0
        for key, value in store_dict.items():
            if value.to_dict()['__class__'] == args[0]:
                n = n + 1
        print(n)

    def emptyline(self):
        """Handle empty line case
        """
        pass

    def do_create(self, line):
        """Creat command function
        """
        if not line:
            print("** class name missing **")
            return
        args = shlex.split(line)
        if args[0] not in self.class_mapping:
            print("** class doesn't exist **")
        else:
            new_model = self.class_mapping[args[0]]()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """show command function
        """
        if not line:
            print("** class name missing **")
            return
        args = shlex.split(line)
        if args[0] not in self.class_mapping:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        store_dict = storage.all()
        for key, value in store_dict.items():
            if value.to_dict()['__class__'] == args[0]:
                if value.to_dict()['id'] == args[1]:
                    print(value)
                    return
        print("** no instance found **")

    def do_destroy(self, line):
        """destroy command function
        """
        if not line:
            print("** class name missing **")
            return
        args = shlex.split(line)
        if args[0] not in self.class_mapping:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        store_dict = storage.all()
        for key, value in store_dict.items():
            if value.to_dict()['__class__'] == args[0]:
                if value.to_dict()['id'] == args[1]:
                    del store_dict[key]
                    storage.save()
                    storage.reload()
                    return
        print("** no instance found **")

    def do_all(self, line):
        """all command function
        """
        if not line:
            print("** class name missing **")
            return
        args = shlex.split(line)
        if args[0] not in self.class_mapping:
            print("** class doesn't exist **")
        else:
            lst = []
            store_dict = storage.all()
            for key, value in store_dict.items():
                if value.to_dict()['__class__'] == args[0]:
                    lst.append(str(value))
            if lst:
                print(lst)

    def do_update(self, line):
        """update command function
        """
        if not line:
            print("** class name missing **")
            return
        args = shlex.split(line)
        if args[0] not in self.class_mapping:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        store_dict = storage.all()
        for key, value in store_dict.items():
            if value.to_dict()['__class__'] == args[0]:
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
    """Main function for the console"""
    HBNBCommand().cmdloop()