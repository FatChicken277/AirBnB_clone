# AirBnB Clone - Console
This project is the console part of a soon to be fully functional AirBnB clone for the Holberton School academy of coding
```
## Usage
```bash
./console.py # Use this to run the console, after that:
```
```bash
quit # Use this command to quit the console
help <command> # This will display information about the command
create <class> # This will create a new object of the available classes
<class>.<command>(<Optional: id> <Optional: attribute/Dictionary> <Optional: Value>
# This format will allow the user to choose an available class and command while passing parameters  to it
<command> <class> <Optional> #This is an alternative for the previous format to input an available command
```
## Non Interactive example
```Bash
echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```
## Avaiable classes (models) and commands
### Commands:
```show``` Displays information about an specific instance of a class: ```show <class> <id>```
```all``` Displays information about all available instances or all instances from an specific class: ```all <Optional: class>```
```update``` Updates the attributes from an specific instance: ```update <class> <id> <Name of attribute or dictionary -Only available in the other format> <Not necessary in case of dictionary: Value of attribute```
```destroy``` Eliminates an instance: ```destroy <class> <id>```
```count``` Displays how many instances of a class are available: ```count <class>```
### Classes
```
BaseModel
User
City
Amenity
State
Place
Review
```
## File Storage
Flow of serialization-deserialization is:
```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
```
Handled in the engine folder.
## Tests
All the tests were made with the module unittest, these are stored in the folder test_models
## Authors
[Alejandro Ramirez](https://github.com/FatChiken277)
[Sebastian Escobar](https://github.com/Katorea132)
