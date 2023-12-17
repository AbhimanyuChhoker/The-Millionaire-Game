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

current_location = "home"
places = {
    "home": 0,
    "office": 10,
    "friend's house": 5,
    "petrol pump": 8,
    "grocery store": 3,
    "supermarket": 7,
    "ikea": 7,
}

supermarket_items = {
    "t-shirt": 25,
    "jeans": 25,
    "sweater": 30,
    "shoes": 40,
    "hat": 10,
    "socks": 5,
    "jacket": 45,
    "dress": 35,
    "scarf": 12,
    "soap": 3,
    "toothbrush": 2,
    "toothpaste": 2,
    "shampoo": 5,
    "conditioner": 4,
    "razor": 4,
    "coffee": 10,
    "tea": 4,
    "bread": 3,
    "butter": 3,
    "jam": 3,
    "yogurt": 1,
    "cereal": 4,
    "toilet paper": 1,
    "laundry detergent": 5,
    "dish soap": 2,
    "broom": 10,
    "trash bags": 3,
    "light bulbs": 1,
    "batteries": 4,
    "band-aids": 1,
    "pain reliever": 3,
    "vitamins": 7,
}
ikea_items = {
    "table": 150,
    "chair": 50,
    "sofa": 500,
    "bookshelf": 80,
    "shoerack": 40,
    "bed": 300,
    "dining table": 250,
    "cupboard": 200,
    "tv furniture": 180,
    "lighting": 30,
    "dressers": 120,
}
inventory_items = {}

# Print welcome message and game instructions
print("Welcome to The Millionaire Game!!")
print(
    f"In this game, you will have to earn a million dollars and retire before you are {RETIREMENT_AGE} years old."
)
print(f"You will start the game with $1000. Choose your career wisely. Good Luck!")


def get_user_input(prompt, valid_choices, value_type):
    """Gets user input with validation."""
    while True:
        user_input = input()
        if value_type == "int":
            user_input = int(input(prompt))
        elif value_type == "str":
            user_input == str(input(prompt))
        if value_type == "str" and user_input.lower() in valid_choices:
            return user_input.lower()
        elif value_type == "int" and user_input in valid_choices:
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
    print(
        "Firstly, you will have to get a house. You can rent a house first and then later in the game you can buy it. It will take the broker around two days for search for a house."
    )
    day += 2
    print("The available house options are: ")
    for house in house_options:
        print(
            f"House 1 - Rent: {house[-1]}, Is Furnished: {house[1]}, Number of Rooms:{house[0]}"
        )
    print("Please enter your house choice number[1, 2, 3, 4, 5]: ")
    house_choice_num = get_user_input(
        "Please enter your house choice number[1, 2, 3, 4, 5]: ", [1, 2, 3, 4, 5], "int"
    )
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
    if destination not in places.keys():
        print(f"Sorry, {destination} is not a valid destination.")
        return

    if destination == current_location:
        print("You are already at your destination.")
        return

    cost_of_travel = places[destination]

    if money >= cost_of_travel:
        money -= cost_of_travel
        print(f"Successfully booked a cab to {destination}! Remaining money: {money}")
    else:
        print(
            f"Insufficient funds. You need at least {cost_of_travel} money to travel to {destination}."
        )


def buy(supermarket_items, money):
    while True:
        shop_type = get_user_input(
            "Please enter the shop which you want to visit[supermarket, grocery store]",
            ["supermarket", "ikea"],
            "str",
        )
        if shop_type.lower() == "supermarket":
            shop_type = "supermarket"
            book_cab(money, "supermarket")
            print("You can buy the following items: ")
            options = supermarket_items.keys()
            price = supermarket_items.values()
        elif shop_type.lower() == "ikea":
            shop_type = "ikea"
            book_cab(money, "ikea_items")
            print("You can buy the following items:")
            options = ikea_items.keys()
            price = ikea_items.values()
        for item in options:
            print(f"{item.title()}: ${price}")
        options.append("exit")
        choice = get_user_input(
            "Please enter the item you want to buy or exit to leave the shop: ",
            options,
            "str",
        )
        if choice.lower() == "exit":
            break
        else:
            money -= shop_type[choice.lower()]
            inventory_items[item] += 1


def setup_house(selected_house):
    isFurnished = selected_house[1]
    if isFurnished:
        print(
            "Your house is already furnished. But you will have to buy some essentials like food, clothes, etc."
        )
        print("To buy that you will have to go to a shop.")
        buy()
        print("Your house is now ready to move in.")
    elif not isFurnished:
        print("Your house is not ready to move in. You will need to buy furniture.")
        print(
            "To buy furniture you will have to go to ikea and to buy essentials like food, clothes, etc."
        )
        buy()
        print("Your house is now ready to move in.")


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
