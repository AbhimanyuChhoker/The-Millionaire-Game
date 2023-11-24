import os
import random

RETIREMENT_AGE = 60
NUM_HOUSE_OPTIONS = 5
WORK_TIME = 8

# Initial game state
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

# Locations and travel costs
places = [
    "home",
    "office",
    "friend's house",
    "petrol pump",
    "grocery store",
    "supermarket",
    "ikea"
]
current_location = "home"
travel_costs = {
    "home": 0,
    "office": 10,
    "friend's house": 5,
    "petrol pump": 8,
    "grocery store": 3,
    "supermarket": 7,
    "ikea": 7
}

# Print welcome message and game instructions
print("Welcome to The Millionaire Game!!")
print(
    f"In this game, you will have to earn a million dollars and retire before you are {RETIREMENT_AGE} years old."
)
print(f"You will start the game with $1000. Choose your career wisely. Good Luck!")


def get_user_input(prompt, valid_choices, value_type):
    """Gets user input with validation."""
    while True:
        if value_type == "int":
            user_input = int(input(prompt))
        elif value_type == "str":
            user_input == str(input(prompt))
        if value_type=="str" and user_input.lower() in valid_choices:
            return user_input.lower()
        elif value_type=="int" and user_input in valid_choices:
            return user_input
        else:
            print(f"That choice is not valid. Please try again.")


def career_chooser():
    """Allows the user to choose a career."""
    global current_career
    print("To earn a million dollars, you will have to get a job")
    print("The available career choices are: ")
    for career in careers:
        print(career)
    while True:
        career_choice = get_user_input("Please enter your choice: ", lower_case_careers)
        if career_choice in lower_case_careers:
            current_career = career_choice
            break
        else:
            print(f"The {career_choice} you entered is not valid. Please try again.")
    print(f"Your career choice is {current_career}.")
    return True


# Set the risk factor based on the chosen career
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

        house_option = [num_rooms, is_furnished, rent]
        house_options.append(house_option)

    return house_options


def get_house(day):
    house_options = get_house_options(NUM_HOUSE_OPTIONS)
    print("Firstly, you will have to get a house. You can rent a house first and then later in the game you can buy it. It will take the broker around two days for search for a house.")
    day += 2
    print("The available house options are: ")
    for house in house_options:
        print(f"House 1 - Rent: {house[-1]}, Is Furnished: {house[1]}, Number of Rooms:{house[0]}")
    print("Please enter your house choice number[1, 2, 3, 4, 5]: ")
    house_choice_num = get_user_input("Please enter your house choice number[1, 2, 3, 4, 5]: ", valid_choices=[1, 2, 3, 4, 5])
    house = house_options[house_choice_num - 1]
    return house  


# Convert twenty-four hour format to twelve hour format
def twenty_four_to_twelve_hour(time):
    hours, minutes = divmod(time, 100)
    time_period = "AM" if hours < 12 else "PM"
    if hours > 12:
        hours -= 12
    return f"{int(hours):02d}:{minutes:02d} {time_period}"


# Book a cab to the specified destination and update the money
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

def buy():
    return True
    #TODO: To be completed today

def setup_house(selected_house):
    isFurnished = selected_house[1]
    if isFurnished:
        print("Your house is already furnished. But you will have to buy some essentials like food, clothes, etc.")
        print("To buy that you will have to go to a supermarket.")
        book_cab(money, "supermarket")
        buy() # To be completed 
        # Rest to be completed afe


# Simulate work by updating the time
def work():
    global time
    print("Working")
    time_taken = WORK_TIME * work_efficiency
    minutes += time_taken
    hours += minutes // 60
    minutes = minutes % 60
    time += time_taken


def working_day():
    global current_location
    if day == 0 and current_career != "startup founder":
        print(
            "This is your first working day. You currently don't have any means of transport. You can take a cab."
        )
        book_cab(money, "office")
        print("Now you can start working.")
        work()

        print(f"It's {twenty_four_to_twelve_hour(time)} in the evening.")
        current_location = "office"


def main():
    career_chooser()
    get_job_stability(current_career)
    global selected_house
    selected_house = get_house(day)
    setup_house(selected_house)
    print(f"Selected house details: {selected_house}")
    working_day()


if __name__ == "__main__":
    main()
