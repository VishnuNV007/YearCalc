'''Write a program that asks the user to enter their name and their age. 
Print out a message that greets them and that tells them the year that they will turn 100 years old.
'''

from distutils.errors import DistutilsTemplateError
from unicodedata import name

import datetime
name=input("Enter your namec :-")
age=int(input("Enter your age :-"))
currentyear=datetime.datetime.now().year
dob=currentyear-age
print(dob+100)


'''age=22
current year=2022
2022-22=2000
dob=2000
2000+100=2100'''

