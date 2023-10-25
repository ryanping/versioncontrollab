# Ryan Tram
# Function passes in a String and returns a string but each digit is incremented by 3 (unless it flows over)
def encode(password):
    password_temp = list(password)
    password_encoded = ""
    for index in range(0,len(password_temp)):
        password_temp[index] = int(password_temp[index])
        password_temp[index] += 3
        if password_temp[index] >= 10:
            password_encoded += str(password_temp[index])[1]
        else:
            password_encoded += str(password_temp[index])
    return(password_encoded)


def decode(encoded_password):
    password_temp = list(encoded_password)
    password_decoded = ""
    for index in range(0, len(password_temp)):
        password_temp[index] = int(password_temp[index])
        password_temp[index] -= 3
        if password_temp[index] <= -1:
            password_decoded += str(password_temp[index] + 10)
        else:
            password_decoded += str(password_temp[index])
    return password_decoded


def main():
    user_continue = True
    while user_continue:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        
        user_menu_option = int(input("Please enter an option: "))
        if user_menu_option == 1:
            user_password = input("Please enter your password to encode: ")
            user_password = encode(user_password)
            print("Your password has been encoded and stored!")
        elif user_menu_option == 2:
            decoded_password = decode(user_password)
            print(f"The encoded password is {user_password}, and the original password is {decoded_password}.")
        elif user_menu_option == 3:
            break


if __name__ == '__main__':
    main()
