# This code is a quiz.It asks you your name and age, also gives you your score as you go.
import easygui
import easygui
player_score = str (0)
easygui.msgbox("Hi welcome to my quiz")
easygui.msgbox("This quiz is about Formula one! Test your knowledge")
player_age = easygui.integerbox("how old are you?")
if player_age <= 18 and player_age >= 15:
    easygui.msgbox("You are old enough for this quiz")
    easygui.msgbox("Welcome to the F1 quiz")
    player_name = easygui.enterbox("Hi What is your name?")
    easygui.msgbox(" Hi " + str(player_name) + " Welcome to the F1 quiz ")
    easygui.msgbox (" Your score is " + player_score + " You will get your final score at the end ")
    easygui.msgbox("First question")
    answer = easygui.choicebox("What year did Daniel Riccardo lose his seat?",choices = ["2021", "2022", "2023","2024"] )
if answer == "2024":
    easygui.msgbox(" Great work! you got the answer right")
    player_score += 1  
else: 
    easygui.msgbox("Sorry you got it wrong")
        easygui.msgbox("Sorry you got it wrong")
answer = easygui.choicebox("How long is Max Verstappen's contract ",choices = ["Until 2028", "Until 2027", "Until 2026", "Until 2025"])
if answer == "Until 2028":
        easygui.msgbox("Great work! you got it right")
        player_score +=1
else:
        easygui.msgbox("Sorry you got it wrong")
answer = easygui.choicebox("Who is the richest formula 1 driver?",choices = ["Lewis", "Charles", "Yuki","Lance"])
if answer == "Lewis":
        easygui.msgbox("Great work! you got it right")
        player_score +=1
else:
        easygui.msgbox("Sorry you got it wrong")
answer = easygui.choicebox("In what year did formula 1 begin",choices = ["1940","1950","1960","1970"])
if answer == "1950":
        easygui.msgbox("Great work! you got it right")
        player_score +=1
else:
        easygui.msgbox("Sorry you got it wrong")

if player_age > 18 or player_age < 15:
    easygui.msgbox("You're not old enough to do this quiz.")    


