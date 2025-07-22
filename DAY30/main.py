# try except else finally pattern

try :
    file = open("data.txt")
    file.read()

    dictionary_ = {"key": [1, 3, 44, 5]}
    print(dictionary_["key"])


except FileNotFoundError:
    file = open("data.txt", "w")
    file.write("Hello Except Block")

except KeyError as error_message:
    print(f"The key {error_message} does not exist")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File was closed")