# This code is a quiz.It asks you your name and age, also gives you your score as you go.
import easygui
easygui.msgbox("Hi welcome to my quiz")
easygui.msgbox("This quiz is about Formula one! Test your knowledge")
age = 15
player_age = int(easygui.enterbox("how old are you?"))
if player_age <= 18 and player_age >= 15:
    easygui.msgbox("You are old enough for this quiz")
    easygui.msgbox("Welcome to the F1 quiz")
else:
    easygui.msgbox("You're not old enough to do this quiz.")    
player_name = easygui.enterbox("Hi What is your name?")
easygui.msgbox(" Hi "+ player_name +" Welcome to the F1 quiz ")
easygui.msgbox("First question")
