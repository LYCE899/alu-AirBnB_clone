# alu-AirBnB_clone
# Project Description & Summary 📝
This project aims to create a replica of the AirBnb website, focusing on both the client side (front-end) and the server side (APIs, database, etc.). However, it will be implemented as a simplified version that can only be accessed through a console or command interpreter.

# The Command Interpreter 💻
The console functions similarly to a shell but with limited capabilities. Its purpose is to execute commands related to the project's objects. The available commands include:

- Creating a new object (e.g., a new User or a new Place)
- Retrieving an object from a file, database, etc.
- Performing operations on objects (e.g., counting, computing stats)
- Updating attributes of an object
- Deleting an object
- Exiting the interpreter

# Starting the Interpreter 🚀
To launch the interpreter, execute the following command:

$ ./console.py

# Using the Interpreter 🔁
Command    Action    Output
help       Displays documented commands    (hbnb) help
help create (any command)    Creates an object of a given class    (hbnb) help create
quit       Ends the command interpreter    (hbnb) quit
EOF        Exits the program    (hbnb) EOF
all        Shows all objects of a given class    (hbnb) all <class>
show       Displays an object of a given class    (hbnb) show <class> <id>
update     Modifies an object of a given class    (hbnb) update <class> <id> <attribute name> <"attribute value">
destroy    Deletes an object of a given class    (hbnb) destroy <class> <id>

Tests 🛰️
To run unit tests on the codebases, execute the following command:

$ python3 unittest -m discover tests
