# calculator.py ReadMe

### What it is and what it does

This is a simple calculator program which takes two integers from user input and performs one of four user-selected arithmetical calculations on them. The user can choose to add them together, subtract the second from the first, multiply them together or divide the first by the second. The main aim of the project was actually to practice defensive programming so that if the user tries to enter strings or floats instead of integers, the program, instead of crashing will remind the user what they should do and give them another chance. In addition, the program allows the user to view their calculations by writing them to a text file and then displaying it. Asking the user to create a second file and, later, to enter the name of it to display the contents was to provide further practice with exception handling, namely the FileNotFoundError if the user enters the wrong filename.

### Installation

Should you wish to install **calculator.py**, please follow these instructions.

You will need to have Python installed on your computer to run this program. If you don’t, go to https://www.python.org and install the most up-to-date version of Python from there.

First, click the ‘Go to file’ button at the top of the repo contents.

![go to file]( https://user-images.githubusercontent.com/133882174/246662973-3a5c499d-446d-4f32-a161-08a5083cd38d.png)
Next, right click the Raw button at the top right of the file. 
![raw button]( https://user-images.githubusercontent.com/133882174/246663018-a66c8dba-1e8e-4bec-8d8c-e62038bd8485.png)
Select ‘Save link as… and save the file to whichever location you want on your computer. Now you can run the program. 

### How to use the project

As was mentioned in the introduction, this is a simple calculator application. Start running the program and it will ask you a number. Type in an integer, tap return and it will ask you for another. Tap return again and it will ask you what sort of calculation you want to perform, ‘a’ for addition, ‘s’ for subtraction, ‘m’ for multiplication and ‘d’ for division. The console will display the result of your calculation and then you will have the opportunity to perform another or enter 00 to stop. Your calculations are written to a text file which is displayed when you have finished. As was explained at the beginning, you will also be asked to provide a name for a new text file which will display your calculations. When you have finished, the program will delete the text files and you will be able to start afresh.
![simple calculation](https://github.com/jeremyTh635/finalCapstone/assets/133882174/1605e47c-9683-460f-afca-a13714a39dcd)
![text output](https://github.com/jeremyTh635/finalCapstone/assets/133882174/071dbc1a-7b4a-4b25-a88f-c2a1d35dc7fb)

### Credits

This program was built by myself working without any collaborators.

