#!/usr/bin/python3
"""Contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


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
            line_list = arg.split()
            new_object = eval(line_list[0])()
            storage.save()
            print(new_object.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the
            class name and id.
        """

        if not self.input_validation(arg):
            return

        if not self.check_id(arg):
            return

        if not self.check_instance(arg):
            return

        line_list = arg.split()
        key = f"{line_list[0]}.{line_list[1]}"
        all_objects = storage.all()
        print(all_objects[key])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
            (save the change into the JSON file).
        """

        if not self.input_validation(arg):
            return

        if not self.check_id(arg):
            return

        if not self.check_instance(arg):
            return

        line_list = arg.split()
        key = f"{line_list[0]}.{line_list[1]}"
        all_objects = storage.all()
        del all_objects[key]
        storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances based or
            not on the class name.
        """
        line_list = arg.split()

        if len(line_list) == 0:
            all_objects = storage.all()
            list_objects = [str(all_objects[key]) for key in all_objects]
            print(list_objects)
        else:
            try:
                class_name = eval(line_list[0])
                all_objects = storage.all()
                list_objects = [str(all_objects[key])
                                for key in all_objects
                                if isinstance(all_objects[key], class_name)]
                print(list_objects)
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
            or updating attribute (save the change into the JSON file)
        """
        if not self.input_validation(arg):
            return
        if not self.check_id(arg):
            return
        if not self.check_instance(arg):
            return
        if not self.check_attribute_name(arg):
            return
        if not self.check_attribute_value(arg):
            return

        line_list = arg.split()
        attribute_name, attribute_value = line_list[2], line_list[3]
        attribute_value = attribute_value[1:-1]
        try:
            attribute_value = eval(attribute_value)
        except NameError:
            pass
        finally:
            objs_dict = storage.all()
            key = f"{line_list[0]}.{line_list[1]}"
            setattr(objs_dict[key], attribute_name, attribute_value)
            objs_dict[key].save()

    @staticmethod
    def input_validation(arg):
        """Validates Input arguments
        """

        line_list = arg.split()
        # Check if any argument is passed
        if (len(line_list) <= 0):
            print("** class name missing **")
            return False
        # Check if argument is a valid class
        try:
            eval(line_list[0])
            return True
        except NameError:
            print("** class doesn't exist **")
            return False

    @staticmethod
    def check_id(arg):
        """Check if their is an input id

        Returns:
            [bool]: If input id exists then True, if not False
        """
        line_list = arg.split()
        if len(line_list) < 2:
            print("** instance id missing **")
            return False
        return True

    @staticmethod
    def check_instance(arg):
        """Check if the input id is corresponding of an existing object

        Returns:
        [bool]: If id's object exists then True, if not False
        """
        line_list = arg.split()
        key = f"{line_list[0]}.{line_list[1]}"
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return False
        return True

    @staticmethod
    def check_attribute_name(arg):
        """Check if there is an existing attribute

        Returns:
        [bool]: If attribute exists ten True, if not False
        """
        line_list = arg.split()
        if len(line_list) < 3:
            print("** attribute name missing **")
            return False
        return True

    @staticmethod
    def check_attribute_value(arg):
        """Check if there is an existing attribute value

        Returns:
        [bool]: If attribute value exists ten True, if not False
        """
        line_list = arg.split()
        if len(line_list) < 4:
            print("** value missing **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
