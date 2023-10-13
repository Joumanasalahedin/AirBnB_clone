#!/usr/bin/python3
"""Defines the console"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the AirBnB command interpreter"""
    prompt = "(hbnb) "

    def emptyline(EOF):
        """Do nothing on an empty line"""
        pass

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit program when EOF is reached"""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of a given class"""
        pass

    def do_show(self, arg):
        """Prints the string representation of an instances"""
        pass

    def do_destroy(self, arg):
        """Destroys an instance"""
        pass

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        pass

    def do_update(self, arg):
        """Updates an instance by adding or updating an attribute"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()