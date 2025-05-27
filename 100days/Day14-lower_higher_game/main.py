from game_data import data
from random import choice
# from art import vs, logo # NO need for ascii files here

# TODO Get random name, desc and country from data list (A)
# TODO get another one ^ (B)
# TODO if user is correct:
## make B follower an A option for next choice
## add correct guess to the TOTAL_SCORE (that starts at 0)
## ask again (loop)
# TODO if user is wrong - end game (show result of comparison and TOTAL_SCORE)
def get_followers_details(data_list: list) -> tuple:
    random_entry = choice(data_list)
    return random_entry['name'], random_entry['description'], random_entry['country'], random_entry['follower_count']

name_A, description_A, country_A, followers_A  = get_followers_details(data) # unpacking in Python
name_B, description_B, country_B, followers_B  = get_followers_details(data)

# ask user for input - compare their followers
# print(logo)
print(f"Compare A: {name_A}, a {description_A}, from {country_A}.")
# print(vs)
print(f"Against B: {name_B}, a {description_B}, from {country_B}: ")
user_choice = input("Who has more followers? type 'a' or 'b': ").lower()



def is_correct_guess() -> bool:
    """Check if user guess of followers number is correct"""
    if followers_A > followers_B and user_choice == "a":
        return True
    elif followers_B > followers_A and user_choice == "b":
        return True
    return False

total_score = 0
while is_correct_guess():
    print("\n" * 20) # clean screen lol
    # print(logo)
    total_score +=1
    print(f"Current score: {total_score}")
    name_A, description_A, country_A, followers_A = name_B, description_B, country_B, followers_B
    print(f"Compare A: {name_A}, a {description_A}, from {country_A}.")
    name_B, description_B, country_B, followers_B = get_followers_details(data)
    # print(vs)
    print(f"Against B: {name_B}, a {description_B}, from {country_B}. ")
    # print(name_A, followers_A) # for debugging purpose only
    # print(name_B, followers_B) # for debugging purpose only
    user_choice = input("Who has more followers? type 'a' or 'b': ").lower()
else:
    print("\n========================================================")
    print(f"That's not correct, your final score is {total_score},\n"
          f"The followers number of {name_A} is {followers_A}, followers number of {name_B} is {followers_B}")

# possible enhancement: add chosen A_names to list so they do not appear again
# refactor : different while loop so the prints are not repeated out of loop
