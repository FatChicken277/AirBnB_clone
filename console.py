#!/usr/bin/python3
"""This module contains a simple console code.
"""
import cmd
import json
from re import search
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """This class Contains all command interpreter.
    """
    prompt = '(hbnb) '
    __models = {"BaseModel": BaseModel, "User": User, "State": State,
                "City": City, "Amenity": Amenity, "Place": Place,
                "Review": Review}

    def precmd(self, comm):
        """This checks for different syntax before
line interpretation

        Returns:
        str: Modified line of command
        """
        met = ["count", "destroy", "all", "show", "update"]
        lili = comm.replace(", ", ",")
        lili = lili.replace(": ", ":")
        lili = lili.split()
        trex = r"\w+[.]\w+\(.*\)$"
        if comm and lili and search(trex, lili[0]):
            lili = lili[0].split(".", 1)
            lilium = lili[1].replace("(", " ")
            lilium = lilium.replace(")", "")
            lilium = lilium.split(" ")
            if lilium[0] in met:
                if len(lilium) > 1:
                    lilista = lilium[1].split(",", 1)
                    if len(lilista) > 1 and lilista[1][0] != "{":
                        lilista = lilium[1].split(",")
                        flag = 1
                    lilista[0] = lilista[0].replace('"', '')
                    if len(lilista) > 2 and flag == 1:
                        lilista[1] = lilista[1].replace('"', '')
                    lilista = " ".join(lilista)
                    comm = "{} {} {}".format(lilium[0], lili[0], lilista)
                else:
                    comm = "{} {}".format(lilium[0], lili[0])
        return comm

    def do_quit(self, args):
        """quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """Does nothing when empty line
        """
        pass

    def do_create(self, args):
        """create command to create a new instance, saves it
            (to the JSON file) and prints the id
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in HBNBCommand.__models:
            new = HBNBCommand.__models[args[0]]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, what):
        """show command to prints the string representation of an instance
            based on the class name and id
        """
        if what:
            lili = what.split()
            if lili[0] not in HBNBCommand.__models:
                print("** class doesn't exist **")
            elif len(lili) > 1:
                Key = "{}.{}".format(lili[0], lili[1])
                if Key in storage.all():
                    print(storage.all()[Key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, what):
        """destroy command to detroys a object based on class name and id
        """
        if what:
            lili = what.split()
            if lili[0] not in HBNBCommand.__models:
                print("** class doesn't exist **")
            elif len(lili) > 1:
                Key = "{}.{}".format(lili[0], lili[1])
                if Key in storage.all():
                    del storage.all()[Key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, what):
        """all command to prints all string representation of all instances
            based or not on the class name
        """
        if what:
            lili = what.split()
            if lili[0] not in HBNBCommand.__models:
                print("** class doesn't exist **")
            else:
                print([str(val) for key, val in storage.all().items()
                       if type(val).__name__ == lili[0]])
        else:
            print([str(val) for key, val in storage.all().items()])

    def do_update(self, what):
        """update command to updates an instance based on the class name and
            id by adding or updating attribute
        """
        if what:
            lili = what.split()
            leni = len(lili)
            if lili[0] not in HBNBCommand.__models:
                print("** class doesn't exist **")
                return
            if leni > 1:
                key = "{}.{}".format(lili[0], lili[1].replace('"', ''))
                if key not in storage.all():
                    print("** no instance found **")
                elif leni > 3:
                    alf, numi = "[a-zA-Z]", r"[0-9]\.[0-9]"
                    if '"' in lili[3]:
                        lili[3] = lili[3].replace('"', '')
                    elif lili[3].isdigit():
                        lili[3] = int(lili[3])
                    elif not search(alf, lili[3]) and search(numi, lili[3]):
                        lili[3] = float(lili[3])
                    lili[2] = lili[2].replace('"', '')
                    setattr(storage.all()[key], lili[2], lili[3])
                    storage.all()[key].save()
                elif leni == 3:
                    if lili[2][0] == "{":
                        lili[2] = lili[2].replace("'", '"')
                        didi = json.loads(lili[2])
                        for k, v in didi.items():
                            setattr(storage.all()[key], k, v)
                        storage.all()[key].save()
                    else:
                        print("** value missing **")
                elif leni == 2:
                    print("** attribute name missing **")
            elif leni == 1:
                print("** instance id missing **")
            return
        print("** class name missing **")

    def do_count(self, name):
        """This counts instances of a class
        """
        print(len([str(val) for key, val in storage.all().items()
                   if type(val).__name__ == name]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
