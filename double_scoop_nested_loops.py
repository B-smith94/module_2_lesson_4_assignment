# Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. 
# The outer loop should iterate over the days, and the inner loop should iterate over the times of the day.
# For each time, randomly select a mood from a predefined list and print it.
# Use the random module again to randomly select the mood.
import random

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 
times = ['morning', 'afternoon', 'evening']

index = 0

for day in days:
    for time in times:
        moods= ['happy', 'sad', 'energetic', 'calm']
        mood = random.choice(moods)
        print(f"On {day} {time} you were {mood}.")
    index += 1
