import os
import random

money = 1000
happiness = 100
energy = 100
currentCareer = "jobless"
careers = ["Labourer", "Shopkeeper", "Startup"]
lowerCaseCareers = ["labourer", "shopkeeper", "startup "]
lowRiskCareers = ["labourer"]
medRiskCareers = ["shopkeeper"]
highRiskCareers = ["startup founder"]
risk = 0



def intro():
    print("Welcome to The Millionaire Game!!")
    print(
        "In this game you will have to earn a million dollars and retire before you are 60 years old."
    )
    print(
        "You will get a thousand dollars to start the game with. You can choose your careers. Good Luck!"
    )


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
    if currentCareer in lowRiskCareers:
        risk = 0.1
    elif currentCareer in medRiskCareers:
        risk = 0.4
    elif currentCareer in highRiskCareers:
        risk = 0.7
    return True


def rentHouse():
    return Pass
    

def getHouseOptions(numOfOptions):
    houseOptions = []
    roomOptions = [1, 2, 3, 4, 5]
    furnishedOptions = [True, False]
    minRent = 500
    maxRent = 1000
    minRentFurnished = 800
    maxRentFurnished = 2000

    for i in range(numOfOptions):
        num_rooms = random.choice(room_options)
        is_furnished = random.choice(furnished_options)
        rent = random.randint(min_rent, max_rent)
        
        house = {
            "Number of Rooms": num_rooms,
            "Fully Furnished": is_furnished,
            "Rent (per month)": rent
        }
        
        house_options.append(house)

    return house_options

def main():
    intro()
    getJobStability(currentCareer)

