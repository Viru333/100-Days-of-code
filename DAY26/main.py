# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
import csv
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

new_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = pandas.DataFrame(new_dict)

new_code_dict = {row.letter: row.code for (index, row) in code_dict.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter the word: ").upper()
    try:
        code_list = [new_code_dict[l] for l in word]

    except KeyError:
        print("Sorry, only letter in the alphabet please")
        generate_phonetic()

    else:
        print(code_list)

generate_phonetic()