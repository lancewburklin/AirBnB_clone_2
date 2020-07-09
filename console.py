#!/usr/bin/python3
"""
    The prompt and whatnot
    This is where we hide the cheese
    Ian is talking right now
    He's got an i7
    I have an i7 too
    That's crazy
"""
import cmd
from models.base_model import BaseModel
from models import storage as pineapple
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
import os
import sys


objs = pineapple.all()


class HBNBCommand(cmd.Cmd):
    """ This is where the class is and where it belongs """
    prompt = '(hbnb) '
    list_of_classes = ['BaseModel', 'User', 'State',
                       'City', 'Amenity', 'Place', 'Review']

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Quit command line """
        if sys.__stdout__.isatty():
            print()
        return True

    def emptyline(self):
        """ Handles empty line as input, do nothing, get them foodstamps """
        pass

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id. Ex: $ create BaseModel
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg in self.list_of_classes:
            new_model = eval(arg + "()")
            print(new_model.id)
            new_model.save()
            pineapple.reload()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
            Prints the string representation of an instance based
            on the class name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        arg = arg.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] in self.list_of_classes:
            if len(arg) < 2:
                print("** instance id missing **")
            else:
                print(arg[0] + "." + arg[1])
                if arg[0] + "." + arg[1] in objs:
                    print(objs[arg[0] + "." + arg[1]])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id
            (save the change into the JSON file).
            Ex: $ destroy BaseModel 1234-1234-1234.
        """
        arg = arg.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] in self.list_of_classes:
            if len(arg) < 2:
                print("** instance id missing **")
            else:
                if arg[0] + "." + arg[1] in objs:
                    del objs[arg[0] + "." + arg[1]]
                    pineapple.save()
                    pineapple.reload()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
            Prints all string representation of all instances based
            or not on the class name. Ex: $ all BaseModel or $ all.
        """
        if len(arg) == 0:
            for k in objs:
                print(objs[k])
        else:
            if arg in self.list_of_classes:
                for k in objs:
                    if arg in k:
                        print(objs[k])
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id by adding
            or updating attribute (save the change into the JSON file).Ex:
            $ update BaseModel 1234-1234-1234 email "aibnb@holberton.com".
        """
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] in self.list_of_classes:
            if len(arg) < 2:
                print("** instance id missing **")
            else:
                n = arg[0] + "." + arg[1]
                if n in objs:
                    if len(arg) < 3:
                        print("** attribute name missing **")
                    elif len(arg) < 4:
                        print("** value missing **")
                    else:
                        objs[n].__dict__[arg[2]] = arg[3]
                        '''print("SDAS;LDFNASDFLKASD;FLKAJSDF;LKASJDF;LKASJDF;LKASJ")
                        print(objs[n])'''
                        objs[n].save()
                        pineapple.reload()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def precmd(self, line):
        new_string = ""
        count = 0
        items = line.split(".")
        if len(items) > 1:
            command = items[1].split("(")
        for key in self.list_of_classes:
            if line == (key + ".all()"):
                return cmd.Cmd.precmd(self, "all " + key)
            elif line == (key + ".count()"):
                for thing in objs:
                    if key in thing:
                        count = count + 1
                print(count)
                return cmd.Cmd.precmd(self, "\n")
            elif ((len(items) > 1 and len(command) > 1 and
                   command[0] == "show" and key == items[0])):
                if items[0] in self.list_of_classes:
                    for i in command[1]:
                        if i != ")":
                            new_string = new_string + i
                    return cmd.Cmd.precmd(
                        self, "show " + key + " " + new_string)
                elif items[0] == "":
                    print("** class name missing **")
                    return cmd.Cmd.precmd(self, "\n")
                else:
                    print("** class doesn't exist **")
                    return cmd.Cmd.precmd(self, "\n")
            elif ((len(items) > 1 and len(command) > 1 and
                   command[0] == "destroy" and key == items[0])):
                if items[0] in self.list_of_classes:
                    for i in command[1]:
                        if i != ")":
                            new_string = (
                                new_string + i)
                    return cmd.Cmd.precmd(
                        self, "destroy " + key + " " + new_string)
        return cmd.Cmd.precmd(self, line)

'''def main():
    """ Main method, motherfucker """
    HBNBCommand().cmdloop()'''


if __name__ == "__main__":
    HBNBCommand().cmdloop()
