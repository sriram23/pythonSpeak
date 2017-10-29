# Speaking Python Program

Hello World!
I tried to make python to speak the words, that I type in my output console. How is it possible? With the espeak command that can be used in Linux Operating system.
## How to do it?
We require a Linux/Unix operating system. First we need to install the espeak command.
Open the terminal and enter the following command.
```
$sudo apt-get install espeak (For Ubuntu, Mint, Debian distributions)
$sudo dnf install espeak (For Redhat, Fedora distributions)
```
The espeak will be installed on executing the above command. We can test it by using the command
```
$espeak Hello
```
You will hear the voice speaking **“Hello”**. Now it is ok. We are done with espeak.
Now, let us move to the python code. It is a very *simple 8 line code*.
First we need to install idle, where can write the python code.
```
$sudo apt-get install idle
```
We can launch idle by simply typing idle in terminal. In idle, create a new file and save it as speak.py.
For executing Linux commands in idle we import a package called *‘os’*.
**os.system()** is the method used to execute Linux commands.
## The Program
```python
import os
Name = raw_input(“Please Enter your name:”)
os.system(“espeak Hello”+Name+” -s 120") 
print “Please Enter the sentence to speak:” 
os.system(“espeak ‘Please Enter the sentence to speak’ -s 120”) 
sentence = raw_input()
print “You have entered: “+sentence 
os.system(“espeak ‘You have entered”+sentence+”’ -s 120")
```
After typing the program, save the file and run the program.
The program first gets the user’s name and greets him/her. Then it asks for the user to enter the text to speak.
When the user enters the text and hits the return key, the espeak command gets executed and it speaks the text entered by user.
