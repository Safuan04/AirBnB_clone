# AirBnB Clone Project
This project is an AirBnB clone aimed at creating a simplified version of the popular accommodation booking platform. The project is built step by step, with the first step being the implementation of a command interpreter that allows users to manage AirBnB objects such as users, states, cities, places, etc. The command interpreter serves as the foundation for the subsequent phases of the project, including HTML/CSS templating, database storage, APIs, and front-end integration.

### Command Interpreter
The command interpreter is a Python-based tool that enables users to interact with the AirBnB objects through the command line. It provides a simple way to create, update, delete, and manage instances of different classes. The interpreter uses a basic file storage system to save and load instances.

### How to Start the Command Interpreter
To start the command interpreter, follow these steps:

1. Clone the project repository to your local machine.
2. Open a terminal window and navigate to the project directory.
3. cd AirBnB_clone
4. Run the command interpreter script: ./console.py

### How to Use the Command Interpreter
Once the command interpreter is running, you can interact with it by entering commands. Commands generally follow this format:

- command class_name class_id [arguments]
- command: The action you want to perform (create, show, update, destroy, all).
- class_name: The name of the class you want to operate on (User, State, City, Place, etc.).
- class_id: The id of the class you want to operate on (User, State, City, Place, etc.).

### Examples
1. Creating a new User instance:
- create User

2. Showing details of a State instance:
- show State 12345-6789

3. Updating a Place instance:
- update Place 9876-5432 name "Cozy Cabin"

4. Deleting a City instance:
- destroy City 5678-9012

5. Listing all instances of a specific class:
- all Place

### Conclusion
The command interpreter provided in this project offers a starting point for managing AirBnB objects through a simplified command-line interface. As the project progresses, you can build upon this foundation to create a full-fledged AirBnB clone with features like HTML/CSS templates, database storage, APIs, and front-end integration.
