# IST356 Assignment 02 (assignment_02)

## Meta

### Learning Objectives

This assignment will get you working with your first module. It will also test your ability to work with lists, dictionaries, parsing and tokenizing textual data.

### Assignment Layout

The each assignment will have a common layout.

- `code` folder contains our code / application. This is where you will create files and write code.
- `code/solution` folder contains the solution to the assignment, for reference.
- `data` data files folder
- `tests` folder contains code to test our application
- `requirements.txt` contains the packages we need to `pip install` to execute the application code
- `readme.md` contains these instructions
- `.vscode` folder contains VS Code setup configurations for running / debugging the application and tests.
-  `reflection.md` is where you submit your reflection, comments on what you learned, things that confuse you, etc.

### Prerequisites 

Before starting this assignment you must:

Install the assignemnt python requirements:

1. From VS Code, open a terminal: Menu => Terminal => New Terminal
2. In the terminal, type and enter: `pip install -r requirements.txt`


### Running Tests

There is some code and tests already working in this assignment. These are sanity checks to ensure VS Code is configured properly.

1. Open **Testing** in the activity bar: Menu => View => Testing
2. You'll need to install the testing tools. Choose **pytest**
3. Open the **>** by clicking on it next to **assignment_01**. Keep clicking on **>** until you see **test_sould_pass** in the **test_assignment.py**
4. Click the Play button `|>` next to **test_should_pass** to execute the test. 
5. A green check means the test code ran and the test has passed.
6. A red X means the test code ran but the test has failed. When a test fails you will be given an error message and stack trace with line numbers.

## Assignment

In this assignment you will parse text input (from a file) of package sizes into a python list of dictionary. You will write the parsed data out in JSON format.

You must complete the functions in `packaging.py` first and then write the main `program.py` The instructions for each can be found in their respective files.  There isn't a significant amount of code you will need to write but you will need to likely use the tests provided and debugger ro figure out how to produce the correct code.

## Advice

packaging.py

- Function definitions with type hints and doc strings have been written for you. just complete the function body.
- Use the pytest tests to ensure your functions are correct
- The tests will not debug, so set a breakpoint under the `if __name__=='__main__'` section and debug the code that way.

parse packaging function tips:
- Split on "/" to get each item e.g. 12 eggs in 1 carton
- Split each item on " in " to get the unit e.g. 12 eggs

program.py

- loop through the file a line at a time
- don't forget to strip the whitespace from the line before using it
