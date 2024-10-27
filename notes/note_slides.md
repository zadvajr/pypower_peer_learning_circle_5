---
marp: true
theme: gaia
class: lead
size: 4:3
style: |
    img {
        width: 300px;
        height: 300px;
        margin: 0 auto;
        text-align: center;
    }

    section {
        background-color: #FFFFFF;
        color: #080808;
        text-align: justify;

    }
    h2, h3, h4, h5, h6{
        text-align: justify;
    }
---

![AltSchool Africa](../assets/alt_school_logo.jpg)
# School of Engineering
(Backend Engineering - Python)
## PyPower Peer Learning Session
---

## Introduction to Python
- Introduction
- History of Python
- Environmental setup
- Installations and setup
- Dependency management
- Python virtual environment
---

## Functions
- Defining and using functions
- Functions with parameters
- More on functions
---

### Introduction
#### What is Python?
Python is a multi purpose, platform independent, interpreted high level programming language designed to improve code readability, simplicity, and clear and concise code.
#### Who invented it?
```
    Guido Van Rossum
```
---

#### When and how old is Python?
```
Invented in 1989 and Released in 1991. Python is 33 years old.
```
#### Why is it called Python?
```
    It was named after a popular BBC show called "Monty Python". 
```
#### Why Python?
- Extensive library and built-in functionalities
- Large community
- Platform independent
- Easy to learn
---
#### How do I know I have Python Installed?
Open your terminal or command prompt and run:
```cmd
    python --version on windows
    python -V shorter option
    python3 --version on MacOS and Linux
    
    Output:
        C:\Users\zadvajr>python --version
        Python 3.12.3
        C:\Users\zadvajr>
```
---
#### What if I don't have Python or Python not added to path?
You get an error:
```cmd
Output:
        C:\Users\zadvajr>python --version
        'python' is not recognised as an internal or external command, operable program or batch file.
        C:\Users\zadvajr>
```
To install python, go to [www.python.org](https://www.python.org/), navigate to download section and select download.

---
### Environmental setup
- Create a directory where you want to host your project files.
- Open terminal
- Navigate into your dir and run ``` python -m venv env ``` to create a virtual environment.
- To activate ``` source env/bin/activate for linux or mac and env/Script/activate for windows```.
- To deactivate: deactivate
---
### Installations and setup
To install libraries and other dependencies check the next section.
### Dependency management
- Installing requirements
- pip freeze
- pip list
---
### Python virtual environment
Already covered in previous section.
```py
python -m venv env
```
---
## Functions
### What is a function?
Simple put block of code that carries out a specific task.
You may also hear names like:
- methods
- functions
- subrountine
- subprogram
- etc
---
### Defining and using functions
- Function definition
- Function call
- Returning data from a function
- Function return type
- positional arguments
- kwargs *kwargs **kwargs
---
# THANK YOU ALL!
# DANIEL ZADVA JNR