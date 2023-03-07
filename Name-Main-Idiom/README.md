# Python Modules Explained
Python files are called modules and they are identified by the .py file extension. A module can define functions, classes, and variables.

So when the interpreter runs a module, the __name__ variable will be set as  __main__ if the module that is being run is the main program.

But if the code is importing the module from another module, then the __name__  variable will be set to that module’s name.

There is a really nice use case for the __name__ variable, whether you want a file that can be run as the main program or imported by other modules. 

We can use an if __name__ == "__main__" block to allow or prevent parts of code from being run when the modules are imported.

(**References:**)
[Python if __name__ == __main__ Explained with Code Examples](https://www.freecodecamp.org/news/if-name-main-python-example/)
