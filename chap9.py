#! python 3
#this script will write the current date and time to a file named datepass.txt in the user's cwd if the password is entered correctly
#the password is 9999

from datetime import datetime

today = datetime.now()
logFile = open('datepass.txt', "a")

password = '9999'

passint=input('What is the password?')

while passint != password:
    print('Try again')
    passint=input('What is the password?')

else:
    logFile.write(f"Password entered correctly {today}. Congrats.\n")
    print("You friggin did it, go look at the file!")

