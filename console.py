#!/usr/bin/python3
"""Contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter

    Args:
        cmd (Cmd): Instance or subclass of Cmd module
        for line-oriented command interpreters
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
