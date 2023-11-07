import os

money = 1000
happiness = 100
energy = 100
currentCareer = "jobless"
careers = ["Labourer", "Shopkeeper", "Startup founder"]
lowerCaseCareers = [
    "immigration officer",
    "teacher",
    "software developer",
    "doctor",
    "labourer",
    "shopkeeper",
    "startup founder",
]


def intro():
    print("Welcome to The Millionaire Game!!")
    print(
        "In this game you will have to earn a million dollars and retire before you are 60 years old."
    )
    print(
        "You will get a thousand dollars to start the game with. You can choose your careers. Good Luck!"
    )
    os.system("sleep")


def careerChooser():
    print("To earn a million dollars, you will have to get a job")
    print("The available career choices are: ")
    for career in careers:
        print(career)
    print("Please enter your choice:")
    careerChoice = str(input())
    while True:
        if careerChoice.lower() in lowerCaseCareers:
            currentCareer = careerChoice.lower()
            break
        else:
            print("The career you entered is not valid. Please try again.")
            print("The available career choices are: ")
            for career in careers:
                print(career)
            print("Please enter your choice:")
            careerChoice = str(input())
    print(f"Your career choice is {currentCareer}.")
    return True

def getJobStability(currentCareer):
    #TODO for 7th November: Complete the function
    return True


intro()
careerChooser()
