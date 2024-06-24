import datetime
import os

def assess_mood():
    date = str(datetime.date.today())

    if mood_entered(date):
        print("You already entered a mood today")
        return
    
    user_in = True
    valid_mood = ['happy', 'relaxed', 'apathetic', 'sad', 'angry']
    mood_int = {'happy' : 2, 'relaxed' :1, 'apathetic' : 0, 'sad' : -1, 'angry' : -2}
    while user_in:
        user_mood = input("How are you feeling? Happy? Relaxed? Apathetic? Sad? Angry?")
        if (user_mood.lower() in valid_mood):
            user_in = False
        else:
            print("Please input a correct feeling")
    
    mood_num = mood_int[user_mood.lower()]
    store(date, mood_num)
    diagnose()

    

def mood_entered(date):
    if not os.path.exists('data/mood_diary.txt'):
        return False
    with open("data/mood_diary.txt","r") as file:
        lines = file.readlines()
        for this_line in lines:
            if this_line.startswith(date):
                return True
    return False

def store(day, mood_num):
    if not os.path.exists('data'):
        os.makedirs("data")
    with open('data/mood_diary.txt', 'a') as file:
        file.write(f"{day} {mood_num}\n")

def diagnose():
    if not os.path.exists('data/mood_diary.txt'):
        return False
    with open('data/mood_diary.txt', 'r') as file:
        lines = file.readlines()

    if len(lines) < 7:
        return
    
    last_moods = lines[-7:]
    mood_num = []
    for mood in last_moods:
        mood_num.append(int (mood.split()[1]))

    happy = 0
    sad = 0
    apathetic = 0
    for mood in mood_num:
        if mood == 2:
            happy += 1
        elif mood == -1:
            sad += 1
        elif mood == 0:
            apathetic += 1
    
    if happy >= 5:
        diag = "manic"
    elif sad >= 4:
        diag = "depressive"
    elif apathetic >= 6:
        diag = "schizoid"
    else:
        diag = {2 : 'happy', 1 : 'relaxed', 0 : 'apathetic', -1 : 'sad', -2 : 'angry'}.get(round(sum(mood_num)/7))

    print(f"Your diagnosis: {diag}!")

