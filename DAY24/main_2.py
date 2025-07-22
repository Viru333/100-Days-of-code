# # file = open("my_file.txt")
# #
# # contents = file.read()
# # print(contents)
# # file.close()
#
# # with open("my_file.txt") as f:
# #     contents = f.read()
# #     print(contents)
#
# # Deletes everything written in the file and write new text in place of everything
# # with open("my_file.txt", 'w') as f:
# #     f.write("New text 0")
# # Doesn't delete anything, instead add new text to file, here 'a' stands for 'append'
# with open("/my_file.txt", 'w') as f:
#     f.write("New text 0")
#
# with open("/my_file.txt") as f:
#     contents = f.read()
#     print(contents)
PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_files:
    names = names_files.readlines()
    # print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", 'w') as completed_letter:
            completed_letter.write(new_letter)
