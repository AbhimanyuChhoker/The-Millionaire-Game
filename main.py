import os
import random

RETIREMENT_AGE = 60
NUM_HOUSE_OPTIONS = 5

money = 1000
happiness = 100
energy = 100
work_efficiency = 1
time = 700
current_career = "jobless"
careers = ["Startup founder", "Software Developer"]
lower_case_careers = ["startup founder", "software developer"]
low_risk_careers = ["software developer"]
high_risk_careers = ["startup founder"]
risk = 0
day = 0
age = 18
years_before_retirement = RETIREMENT_AGE - age
places = [  
    "home",
    "office",
    "friend's house",
    "petrol pump",
    "grocery store",
    "supermarket",
]
current_location = "home"
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
        f"In this game, you will have to earn a million dollars and retire before you are {RETIREMENT_AGE} years old."
    )
    print("You will start the game with $1000. Choose your career wisely. Good Luck!")


def career_chooser():
    global current_career
    print("To earn a million dollars, you will have to get a job")
    print("The available career choices are: ")
    for career in careers:
        print(career)
    print("Please enter your choice:")
    career_choice = str(input())
    while True:
        if career_choice.lower() in lower_case_careers:
            current_career = career_choice.lower()
            break
        else:
            print("The career you entered is not valid. Please try again.")
            print("The available career choices are: ")
            for career in careers:
                print(career)
            print("Please enter your choice:")
            career_choice = str(input())
    print(f"Your career choice is {current_career}.")
    return True


def get_job_stability(current_career):
    global risk
    if current_career in low_risk_careers:
        risk = 0.1
    elif current_career in high_risk_careers:
        risk = 0.7


def get_house_options(num_of_options):
    house_options = []
    room_options = [1, 2, 3, 4, 5]
    furnished_options = [True, False]
    min_rent = 500
    max_rent = 1000
    min_rent_furnished = 800
    max_rent_furnished = 2000

    for i in range(num_of_options):
        num_rooms = random.choice(room_options)
        is_furnished = random.choice(furnished_options)
        if is_furnished:
            rent = random.randint(min_rent_furnished, max_rent_furnished)
        else:
            rent = random.randint(min_rent, max_rent)

        house_option = f"Number of rooms: {num_rooms}, Fully furnished: {is_furnished}, Rent (per month): {rent}"
        house_options.append(house_option)

    return house_options


def get_house():
    global day
    house_options = get_house_options(NUM_HOUSE_OPTIONS)
    print(
        "Firstly, you will have to have a house. You can rent a house first and then later in the game buy it. It will take the broker around two days to search for a house."
    )
    print("The available house options are: ")
    day += 1
    for i, house in enumerate(house_options, 1):
        print(f"House {i}: {house}")
    print("Please enter your house choice number[1, 2, 3, 4, 5]: ")
    house_choice_num = int(input())
    while True:
        if house_choice_num > NUM_HOUSE_OPTIONS or house_choice_num < 1:
            print("The house you entered is not valid. Please try again.")
            print("The available house options are: ")
            for house in house_options:
                print(house)
            print("Please enter your house choice number[1, 2, 3, 4, 5]: ")
            house_choice_num = int(input())
        else:
            house_choice = house_options[house_choice_num - 1]
            print(f"Your house choice is {house_choice}.")
            break
    return house_choice


def get_house_rent(house_choice):
    house_choice_list = house_choice.split()
    rent = house_choice_list[-1]
    return rent


def twenty_four_to_twelve_hour(time):
    hours = time // 100
    minutes = time % 100
    time_period = "AM"
    if hours >= 12:
        time_period = "PM"
        if hours > 12:
            hours -= 12
    twelve_hour_time = f"{int(hours):02d}:{minutes:02d} {time_period}"
    return twelve_hour_time


def book_cab(money, destination):
    if destination not in places:
        print(f"Sorry, {destination} is not a valid destination.")
        return

    if destination == current_location:
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


def work():
    print("Working")
    time_taken = 800 / work_efficiency
    time += time_taken


def working_day():
    if day == 0 and current_career != "startup founder":
        print(
            "This is your first working day. You currently don't have any means of transport. You can take a cab."
        )
        book_cab(money, "office")
        print("Now you can start working.")
        work()
        print(f"Its {twenty_four_to_twelve_hour(time)} in the evening.")


def main():
    intro()
    career_chooser()
    get_job_stability(current_career)
    house_choice = get_house()
    rent = get_house_rent(house_choice)
    print(twenty_four_to_twelve_hour(time))


main()
