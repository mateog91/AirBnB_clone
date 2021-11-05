#!/usr/bin/python3
"""Contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel


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
        line_list = arg.split()
        if (len(line_list) <= 0):
            print("** class name missing **")
        else:
            try:
                new_object = eval(line_list[0])()
                print(new_object.id)
            except NameError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
