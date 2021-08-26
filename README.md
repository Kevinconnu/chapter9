# chap9
chap9.py is a super-simple python script that writes the current time and date to a file if the preset 'password' is entered correctly.
This script does not handle passwords in any sort of secure or recommended workflow, I was just attempting to understand user input, text comparison, the datetime module, and writing to text files.

## Dependencies
none

## Usage 
```bash
$ git clone https://github.com/Kevinconnu/chapter9.git
$ cd chapter9
$ chmod +x chap9.py
$ python chap9.py
```
All you need to do is enter the password when prompted (default is '9999').
To verify that it worked, check cwd for 'datepass.txt' file. If it worked there will be an line with the time and date you entered the password correctly.
