import os
import random

money = 1000
happiness = 100
energy = 100
currentCareer = "jobless"
careers = ["Labourer", "Shopkeeper", "Startup founder"]
lowerCaseCareers = ["labourer", "shopkeeper", "startup founder"]
lowRiskCareers = ["labourer"]
medRiskCareers = ["shopkeeper"]
highRiskCareers = ["startup founder"]
risk = 0
day = 0
age = 18
yearsBeforeRetirement = 60 - age
places = [
    "home",
    "office",
    "friend's house",
    "petrol pump",
    "grocery store",
    "supermarket",
]
currentLocation = "home"
travel_costs = {
    "home": 0,
    "office": 10,
    "friend's house": 5,
    "petrol pump": 8,
    "grocery store": 3,
    "supermarket": 7,
}


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


def getHouseOptions(numOfOptions):
    houseOptions = []
    roomOptions = [1, 2, 3, 4, 5]
    furnishedOptions = [True, False]
    minRent = 500
    maxRent = 1000
    minRentFurnished = 800
    maxRentFurnished = 2000

    for i in range(numOfOptions):
        numRooms = random.choice(roomOptions)
        isFurnished = random.choice(furnishedOptions)
        if isFurnished:
            rent = random.randint(minRentFurnished, maxRentFurnished)
        else:
            rent = random.randint(minRent, maxRent)

        houseOption = f"Number of rooms: {numRooms}, Fully furnished: {isFurnished}, Rent (per month): {rent}"
        houseOptions.append(houseOption)

    return houseOptions


def getHouse():
    houseOptions = getHouseOptions(5)
    print(
        "Firstly you will have to have a house. You can rent a house first and then later in the game buy it. It will take the broker around two days to search for a house."
    )
    print("The available house options are: ")
    day += 1
    for i, house in enumerate(houseOptions, 1):
        print(f"House {i}: {house}")
    print("Please enter your house choice number[1, 2, 3, 4, 5]: ")
    houseChoiceNum = int(input())
    while True:
        if houseChoiceNum > 5 or houseChoiceNum < 1:
            print("The house you entered is not valid. Please try again.")
            print("The available house options are: ")
            for house in houseOptions:
                print(house)
            print("Please enter your house choice number[1, 2, 3, 4, 5]: ")
            houseChoiceNum = int(input())
        else:
            houseChoice = houseOptions[houseChoiceNum - 1]
            print(f"Your house choice is {houseChoice}.")
            break
    return houseChoice


def getHouseRent(houseChoice):
    houseChoiceList = houseChoice.split()
    rent = houseChoiceList[-1]
    return rent


def bookCab(money, destination):
    if destination not in places:
        print(f"Sorry, {destination} is not a valid destination.")
        return

    if destination == currentLocation:
        print("You are already at your destination.")
        return

    cost_of_travel = travel_costs[destination]

    if money >= cost_of_travel:
        money -= cost_of_travel
        print(f"Successfully booked a cab to {destination}! Remaining money: {money}")
    else:
        print(
            f"Insufficient funds. You need at least {cost_of_travel} money to travel to {destination}."
        )


def workingDay():
    if day == 0:
        print(
            "This is your first working day. You currently don't have any means of transport. You can take a cab."
        )

    return True


def main():
    intro()
    careerChooser()
    getJobStability(currentCareer)
    houseChoice = getHouse()
    rent = getHouseRent(houseChoice)


main()
