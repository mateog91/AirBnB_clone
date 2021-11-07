![hbnb_logo](https://user-images.githubusercontent.com/85451781/140629045-d5b7c5a3-6aed-44ef-ba78-94903444198d.png)

# AirBnB_clone

This project is the first step to build our first complete web application: the AirBnB clone. This project consists in making a shell to manage AirBnB objects, this step is very important because we will use what we build here with all the following projects: HTML/CSS templates, database storage, API, front-end integration...

## Scope:

- Implement a parent class (called BaseModel) that will handle initialization, serialization and de-serialization of your future instances.
- Create a simple serialization/de-serialization flow: Instance <-> Dictionary <-> JSON String <-> File
- Create all the classes used for AirBnB (User, State, City, Place...) that inherit from BaseModel
- Create the first abstract storage engine of the project: File Storage.
- Create all the unittests to validate all our classes and storage engine.

### Object Management:

- Create a new object (e.g. a new user or a new location).
- Retrieve an object from a file, a database, etc.
- Perform operations on objects (count, calculate statistics, etc...)
- Update the attributes of an object
- Destroy an object

## Installation

There is no installation process required, although user needs to clone this repository

```bash
$ git clone https://github.com/mateog91/AirBnB_clone.git
$ cd AirBnB_clone
~/AirBnB_clone$ ./console.py
```

## Usage

The following commands are available for this console:

- **EOF**: Exits console by End of File. Usage: EOF
- **all**: Prints all string representation of all instances based or not on the class name. Usage: all [optional: <class_name>]
- **create**: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Usage: create <class_name>
- **destroy**: Deletes an instance based on the class name and id (save the change into the JSON file). Usage: destroy <class_name> <id>
- **help**: List available commands with "help" or detailed help with "help cmd". Usage: help <command_name>
- **quit**: Quit command to exit the program. Usage: quit
- **show**: Prints the string representation of an instance based on the class name and id. Usage: show <class_name> <id>
- **update**: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Only one attribute can be updated at the time. Usage: update <class_name> <id> <attribute_name> "<attribute_value>"

### Examples

To enter interactive mode use:

```bash
$ ./console.py
```

#### EOF

Interactive Mode:

```bash
(hbnb) EOF
$
```

Non-interactive Mode:

```bash
$ echo "EOF" | ./console.py
$
```

#### create

Interactive Mode:

```bash
(hbnb) create BaseModel
a410391f-8561-444d-b9dd-42fd7ab071cd
(hbnb) create User
f68a2d95-eb43-4d51-8696-b4e8335749ce
(hbnb) create City
6d9108ff-7335-4a18-b40b-0be06bd30003
(hbnb) create Amenity
37ea040e-5b15-4c02-8e4a-55e389bb8d2f
(hbnb) create Place
8218f493-928a-4267-8826-1f589371a1d8
(hbnb) create Review
6424b174-5c19-4ab8-a62d-dd5c08342592
(hbnb) create State
e819f1a7-ed5f-42c8-bace-e5000df65082
(hbnb)
```

Non-interactive Mode:

```bash
$ echo "create State" | ./console.py
(hbnb) 71983287-5a6d-42d4-ab40-7b792a8c3032
(hbnb)
$
```

#### show

Interactive Mode:

```bash
(hbnb) show BaseModel a410391f-8561-444d-b9dd-42fd7ab071cd
[BaseModel] (a410391f-8561-444d-b9dd-42fd7ab071cd) {'id': 'a410391f-8561-444d-b9dd-42fd7ab071cd', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 1, 916017), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 1, 916029)}
(hbnb) show User f68a2d95-eb43-4d51-8696-b4e8335749ce
[User] (f68a2d95-eb43-4d51-8696-b4e8335749ce) {'id': 'f68a2d95-eb43-4d51-8696-b4e8335749ce', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 9, 639435), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 9, 639443)}
(hbnb) show City 6d9108ff-7335-4a18-b40b-0be06bd30003
[City] (6d9108ff-7335-4a18-b40b-0be06bd30003) {'id': '6d9108ff-7335-4a18-b40b-0be06bd30003', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 13, 989203), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 13, 989212)}
(hbnb)
```

Non-interactive Mode:

```bash
$ echo "show Amenity 37ea040e-5b15-4c02-8e4a-55e389bb8d2f" | ./console.py
(hbnb) [Amenity] (37ea040e-5b15-4c02-8e4a-55e389bb8d2f) {'id': '37ea040e-5b15-4c02-8e4a-55e389bb8d2f', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 30, 670818), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 30, 670825)}
(hbnb)
$
```

#### destroy

Interactive Mode:

```bash
(hbnb) destroy State 71983287-5a6d-42d4-ab40-7b792a8c3032
(hbnb) show State 71983287-5a6d-42d4-ab40-7b792a8c3032
** no instance found **
(hbnb)
```

Non-interactive Mode:

```bash
$ echo "destroy Amenity 37ea040e-5b15-4c02-8e4a-55e389bb8d2f" | ./console.py
(hbnb)
(hbnb)
$ echo "show Amenity 37ea040e-5b15-4c02-8e4a-55e389bb8d2f" | ./console.py
(hbnb) ** no instance found **
(hbnb)
$
```

#### all

Interactive Mode:

_With no optional argument_

```bash
(hbnb) all
["[BaseModel] (a410391f-8561-444d-b9dd-42fd7ab071cd) {'id': 'a410391f-8561-444d-b9dd-42fd7ab071cd', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 1, 916017), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 1, 916029)}",
"[User] (f68a2d95-eb43-4d51-8696-b4e8335749ce) {'id': 'f68a2d95-eb43-4d51-8696-b4e8335749ce', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 9, 639435), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 9, 639443)}",
"[City] (6d9108ff-7335-4a18-b40b-0be06bd30003) {'id': '6d9108ff-7335-4a18-b40b-0be06bd30003', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 13, 989203), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 13, 989212)}",
"[Place] (8218f493-928a-4267-8826-1f589371a1d8) {'id': '8218f493-928a-4267-8826-1f589371a1d8', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 36, 401021), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 36, 401027)}",
"[Review] (6424b174-5c19-4ab8-a62d-dd5c08342592) {'id': '6424b174-5c19-4ab8-a62d-dd5c08342592', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 43, 646451), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 43, 646459)}",
"[State] (e819f1a7-ed5f-42c8-bace-e5000df65082) {'id': 'e819f1a7-ed5f-42c8-bace-e5000df65082', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 49, 182285), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 49, 182294)}"]
```

_With optional argument <clase_name>_

```bash
(hbnb) all City
["[City] (6d9108ff-7335-4a18-b40b-0be06bd30003) {'id': '6d9108ff-7335-4a18-b40b-0be06bd30003', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 13, 989203), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 13, 989212)}"]
(hbnb)
```

Non-interactive Mode:

_With no optional argument_

```bash
$ echo "all" | ./console.py
(hbnb) ["[BaseModel] (a410391f-8561-444d-b9dd-42fd7ab071cd) {'id': 'a410391f-8561-444d-b9dd-42fd7ab071cd', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 1, 916017), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 1, 916029)}",
"[User] (f68a2d95-eb43-4d51-8696-b4e8335749ce) {'id': 'f68a2d95-eb43-4d51-8696-b4e8335749ce', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 9, 639435), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 9, 639443)}",
"[City] (6d9108ff-7335-4a18-b40b-0be06bd30003) {'id': '6d9108ff-7335-4a18-b40b-0be06bd30003', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 13, 989203), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 13, 989212)}",
"[Place] (8218f493-928a-4267-8826-1f589371a1d8) {'id': '8218f493-928a-4267-8826-1f589371a1d8', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 36, 401021), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 36, 401027)}",
"[Review] (6424b174-5c19-4ab8-a62d-dd5c08342592) {'id': '6424b174-5c19-4ab8-a62d-dd5c08342592', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 43, 646451), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 43, 646459)}",
"[State] (e819f1a7-ed5f-42c8-bace-e5000df65082) {'id': 'e819f1a7-ed5f-42c8-bace-e5000df65082', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 49, 182285), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 49, 182294)}"]
(hbnb)
$
```

_With optional argument <clase_name>_

$ echo "all Place" | ./console.py
(hbnb) ["[Place] (8218f493-928a-4267-8826-1f589371a1d8) {'id': '8218f493-928a-4267-8826-1f589371a1d8', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 36, 401021), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 36, 401027)}"]
(hbnb)
$

#### update

Interactive Mode:

```bash
(hbnb) show User f68a2d95-eb43-4d51-8696-b4e8335749ce
[User] (f68a2d95-eb43-4d51-8696-b4e8335749ce) {'id': 'f68a2d95-eb43-4d51-8696-b4e8335749ce', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 9, 639435), 'updated_at': datetime.datetime(2021, 11, 7, 13, 56, 9, 639443)}
(hbnb) update User f68a2d95-eb43-4d51-8696-b4e8335749ce first_name "Betty"
(hbnb) show User f68a2d95-eb43-4d51-8696-b4e8335749ce
[User] (f68a2d95-eb43-4d51-8696-b4e8335749ce) {'id': 'f68a2d95-eb43-4d51-8696-b4e8335749ce', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 9, 639435), 'updated_at': datetime.datetime(2021, 11, 7, 14, 33, 51, 916366), 'first_name': 'Betty'}
(hbnb)
```

Non-interactive Mode:

```bash
$ echo "show User f68a2d95-eb43-4d51-8696-b4e8335749ce" | ./console.py
(hbnb) [User] (f68a2d95-eb43-4d51-8696-b4e8335749ce) {'id': 'f68a2d95-eb43-4d51-8696-b4e8335749ce', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 9, 639435), 'updated_at': datetime.datetime(2021, 11, 7, 14, 36, 11, 816926), 'first_name': 'Betty'}
(hbnb)
$ echo "update User f68a2d95-eb43-4d51-8696-b4e8335749ce last_name 'Holberton'" | ./console.py
$ echo "show User f68a2d95-eb43-4d51-8696-b4e8335749ce" | ./console.py
(hbnb) [User] (f68a2d95-eb43-4d51-8696-b4e8335749ce) {'id': 'f68a2d95-eb43-4d51-8696-b4e8335749ce', 'created_at': datetime.datetime(2021, 11, 7, 13, 56, 9, 639435), 'updated_at': datetime.datetime(2021, 11, 7, 14, 37, 34, 566550), 'first_name': 'Betty', 'last_name': 'Holberton'}
(hbnb)
$
```

#### help

Interactive Mode:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
(hbnb) help create
 Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id.

(hbnb)
```

#### quit

Interactive Mode:

```bash
(hbnb) quit
$
```

## Contributing

This is a purely academic project for Holberton School. It cannot be modified and there will be no pull requests.

## Authors

Mateo Garcia - [twitter](https://twitter.com/mateog91) - [linkedin](https://www.linkedin.com/in/mateog91/)
Sandra Calero - [twitter](https://twitter.com/SandraC59631923) - [linkedin](https://www.linkedin.com/in/sandra-liliana-calero/)
Project for [Holberton School](https://www.holbertonschool.com/)
