#!/usr/bin/python3
"""Contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter

    Args:
        cmd (Cmd): Instance or subclass of Cmd module
        for line-oriented command interpreters

    Description:
        You can assume arguments are always in the right order
        Each arguments are separated by a space
        A string argument with a space must be between double quote
        The error management starts from the first argument to the last one
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        quit()
        return True

    def do_EOF(self, arg):
        """End of file
        """
        quit()
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id.
        """
        if not self.input_validation(arg):
            return
        else:
            try:
                line_list = arg.split()
                new_object = eval(line_list[0])()
                print(new_object.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the
            class name and id.
        """
        if not self.input_validation(arg):
            return

        line_list = arg.split()
        if len(line_list) < 2:
            print("** instance id missing **")
            return

        key = line_list[0] + line_list[1]
        all_objects = FileStorage.all
        if key not in all_objects:
            print("** no instance found **")
            return

    @staticmethod
    def input_validation(arg):
        """Validates Input arguments
        """

        line_list = arg.split()
        # Check if any argument is passed
        if (len(line_list) <= 0):
            print("** class name missing **")
            return False
        # Check if argument is BaseModel
        if line_list[0] != BaseModel.__name__:
            print("** class doesn't exist **")
            return False
        # Check if argumen is subclass of BaseModel
        for element in BaseModel.__subclasses__():
            print(element)
            if element.__name__() != line_list[0]:
                print("** class doesn't exist **")
                return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
