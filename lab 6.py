def encode(password):
    # This function encodes the password by shifting each digit up by 3 numbers.
    return "".join(str((int(char) + 3) % 10) for char in password)


def decode(encoded_password):
    #partners function - Ian :)
    output = ''
    for char in encoded_password:
        add = int(char) - 3
        if add < 0:
            add += 10
        output += str(add)
    return output


def main():
    encoded_password = ""
    original_password = ""
    decoded_password = ""  # This will be used in option 2 to show the decoded password
    while True:
        print("Menu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            original_password = input("Please enter your password to encode: ")
            encoded_password = encode(original_password)
            print("Your password has been encoded and stored!")

        elif option == "2":
            if encoded_password:
                decoded_password = decode(encoded_password)  # Your partner will fill in this function
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            else:
                print("No password has been encoded yet.")

        elif option == "3":
            break
        else:
            print("Invalid option. Please try again.")

main()
