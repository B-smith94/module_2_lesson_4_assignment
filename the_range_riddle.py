#Write a program that prints off different moods for each day of the week.
#make a list of moods, including happy, sad, energetic, and calms
#Use the range() function to loop through every day of the week 
#for each day, randomly select a mood from the list and print it
import random


day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 

for index in range(7):
    moods = ['happy', 'sad', 'energetic', 'calm']
    print("On " + day[index] + ", you were feeling " + random.choice(moods) + ".")