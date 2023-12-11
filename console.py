#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class that inherits from cmd.Cmd"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("Quitting...")
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("Quitting...")
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in storage.all():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key not in storage.all()[class_name]:
                print("** no instance found **")
                return
            print(storage.all()[class_name][key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in storage.all():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key not in storage.all()[class_name]:
                print("** no instance found **")
                return
            del storage.all()[class_name][key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.extend(obj.values())
        else:
            class_name = args[0]
            if class_name not in storage.all():
                print("** class doesn't exist **")
                return
            obj_list = list(storage.all()[class_name].values())
        print(obj_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in storage.all():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key not in storage.all()[class_name]:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attribute_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return

            attribute_value = args[3]

            # Convert attribute_value to the appropriate type
            attribute_type = type(getattr(storage.all()[class_name][key], attribute_name))
            try:
                attribute_value = attribute_type(attribute_value)
            except ValueError:
                print("** value missing **")
                return

            setattr(storage.all()[class_name][key], attribute_name, attribute_value)
            storage.save()
        except KeyError:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

