# Jori Rzepecki
def encode(text):
    s = 3
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        result += chr((ord(char) + s - 48) % 10 + 48)
    return result


def decode(text):
    s = 3
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        result += chr((ord(char) - s - 48 + 10) % 10 + 48)
    return result


def main():
    option = 1
    encodedText = ""
    # while loop for when option is not 3
    while option != 3:
        # printing menu and prompting user to select
        print("\nMenu\n------------\n1. Encode\n2. Decode\n3. Quit\n")
        # taking input of option selected
        option = int(input("Please enter an option: "))
        # option 1 asks user to input a password and call encode function
        if option == 1:
            password = input('Please enter your password to encode: ')
            encodedText = encode(password)
            print('Your password has been encoded and stored!')
        # option 2 prints the decoded and original string
        if option == 2:
            decodedText = decode(encodedText)
            print("The encoded password is", encodedText + ", and the original password is", decodedText,".")


if __name__ == '__main__':
    main()