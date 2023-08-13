#!/usr/bin/python3
"""Defining a class called HBNBCommand"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand that treats the commands entered
    by the User
    """

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel,
               "User": User,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Place": Place,
               "Review": Review}

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

    def do_EOF(self, line):
        """Ctrl-D to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_create(self, cls_name):
        """
        Creates a new instance of the BaseModel class and saves it
        to Json file
        """
        if not cls_name:
            print("** class name missing **")
        else:
            target_class = self.classes.get(cls_name)
            if not target_class:
                print("** class doesn't exist **")
            else:
                cls_name = target_class()
                models.storage.save()
                print(cls_name.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
        else:
            cls_name = args[0]
            target_class = self.classes.get(cls_name)
            if not target_class:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                cls_id = args[1]
                key = f"{cls_name}.{cls_id}"
                obj = models.storage.all().get(key)
                if not obj:
                    print("** no instance found **")
                else:
                    print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
        else:
            cls_name = args[0]
            target_class = self.classes.get(cls_name)
            if not target_class:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                cls_id = args[1]
                key = f"{cls_name}.{cls_id}"
                dictionay = models.storage.all()
                obj = models.storage.all().get(key)
                if not obj:
                    print("** no instance found **")
                else:
                    del dictionay[key]
                    models.storage.save()

    def do_all(self, cls_name=None):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        list_instances = []
        all_instances = models.storage.all()
        if cls_name:
            target_class = self.classes.get(cls_name)
            if not target_class:
                print("** class doesn't exist **")
            else:
                for key in all_instances.keys():
                    class_name, class_id = key.split(".")
                    if class_name == cls_name:
                        list_instances.append(f"{str(all_instances[key])}")
                print(list_instances)
        else:
            for key in all_instances.keys():
                list_instances.append(f"{str(all_instances[key])}")
            print(list_instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        cls_name = None
        cls_id = None
        attr_name = None
        attr_val = None

        if len(args) < 1:
            print("** class name missing **")
        else:
            cls_name = args[0]
            target_class = self.classes.get(cls_name)
            if not target_class:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                cls_id = args[1]
                key = f"{cls_name}.{cls_id}"
                obj = models.storage.all().get(key)
                if not obj:
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attr_name = args[2]
                    attr_val = args[3].strip('"')
                    setattr(obj, attr_name, attr_val)
                    models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
