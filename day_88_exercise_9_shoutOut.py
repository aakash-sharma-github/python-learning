# Day 88
# Exercise 9: Solution 
import pyttsx3

name = ["Sudi", "Salina", "sukesh", "Aakash", "rohan"]

# Initilization the text-to-speech engine
engine = pyttsx3.init()

# speaking names through for loop.
for names in name:
    engine.say(f"hello {names} How are you?")
    engine.runAndWait()