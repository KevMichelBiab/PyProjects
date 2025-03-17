import random
from task import Task
from datetime import date

emotions= {
    "happy": [
        "I am glad to hear that 🙂. Don't forget to thank the Lord for your happiness. He is at the origin of everything. "
    ],
    "sad": [
        "I am sorry to hear that 😢. When I am feeling down I like to remind myself that God is always there for me no matter what. There are so many instances in the Bible when He showed us the love He has for us."
    ],
    "stressed": [
        "Life can stressful at times.\nFirst of all, don't beat yourself up for feeling this way it is justified. Sometimes it gets tough.Remember that no matter what God is proud of you. "
    ]
}
quotes = [ 
        "I am the way and the truth and the life. No one comes to the Father except through me - John 14:6", 
        "For I know the plans that I have for you,' declares the Lord 'plans to prosper and not to harm you, plans to give you hope and a future - Jeremiah 29:11",
        "Trust the Lord with all your heart and lean not on your own understanding; in all your ways submit to him, and he will make your paths straight' Proverbs 3:5-6"
          
          ]
tasks_lst = []



def mood_tracker(input: str):
    if input in emotions:
        return emotions[input]

def quotes_generator():
    return random.choice(quotes)

def manage_task():
    return

def add_task(task_added: Task):
    for task in tasks_lst:
        if task_added.id == task.id:
            return
    tasks_lst.append(task_added)

def view_task():
    print(f"Here is the total of your tasks: ")
    for elt in tasks_lst:
        print(elt)

            















def main():
    print("Welcome to Your Daily Life Companion! 😊\n1. Track My Mood\n2. Get Motivation\n3. Manage My Tasks\n4. Chat with Me\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        mood = input("How are you feeling today?📝 - ").lower()
        answer = mood_tracker(mood)
        print(" ".join(answer))
    
    if choice == "2":
        print(quotes_generator())
    
    if choice == "3":
        title = input("Title:")
        date_year = int(input("Year-date:"))
        date_month = int(input("Month-date:"))
        date_day = int(input("Day-date:"))
        date_entered = date(date_year, date_month, date_day)
        description = input("Description: ")
        new_task = Task(title,date_entered,description)
        add_task(new_task)
        view_task()
        
        

main() 
