# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

import pandas
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# data_text = pandas.read_table("nato_ph.txt") # TEST text file
# print(data_text) # TEST text file
data_dict = {row.letter:row.code for index, row in data.iterrows()}
# print(data_dict) # DEBUG

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = input("What is your name? ").upper()
phonetics_in_name = [data_dict[letter] for letter in user_name]
print(phonetics_in_name)
