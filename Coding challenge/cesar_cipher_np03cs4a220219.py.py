def main():
    def welcome():
        print("Welcome to the Caesar Cipher")
        print("This program encrypts and decrypts text with the Caesar Cipher.")

    welcome()

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
    def encryption():
        user_value = input("What message do you want to encrypt:  ")
        user_value = user_value.upper()
        while True:
            try:
                key = int(input("Write the shift key from 1-26:  "))
                if key >= 1 & key <= 26:
                    break
                else:
                    print("Invalid shift.Please enter number from 1-26")
                    continue
            except ValueError:
                print("Invalid shift.Please enter number from 1-26")
                continue

        new_value = ""
        for characters in user_value:  # looping user value and storing in characters 1 by 1 eg: "a","p","l"
            if characters in chars:  # if the user value which was looped can be found in chars then
                position = chars.find(characters) # find the position of the characters(looped user_value) in the chars
                new_position = (position+key) % len(chars)
                new_value += chars[new_position]

            else:
                new_value += characters
                print("New value is ", new_value)
        print(new_value)

    def decryption():
        user_value = input("What message do you to decrypt:  ")
        user_value = user_value.upper()
        while True:
            try:
                key = int(input("Write the shift key from 1-26:  "))
                if key >= 1 & key <= 26:
                    break
                else:
                    print("Invalid shift.Please enter number from 1-26")
                    continue
            except ValueError:
                print("Invalid shift.Please enter number from 1-26")
                continue
      
        new_value = ""
        for characters in user_value:
            if characters in chars:
                position = chars.find(characters)
                new_position = (position-key) % len(chars)
                new_value += chars[new_position]
            else:
                new_value += characters
                print("New value is ", new_value)
        print(new_value)

    def enter_message():
        while True:

            user_choice = input(
                "Would you like to encrypt (e) or decrypt (d): ")
            if user_choice.lower() == "encrypt":
                encryption()
            elif user_choice.lower() == "e":
                encryption()
            elif user_choice.lower() == "decrypt":
                decryption()
            elif user_choice.lower() == "d":
                decryption()
            else:
                print("Invalid choice, Please choose either encrypt (e) or decrypt (d)")
                continue

            loop_terminate = input(
                "Would you like to encrypt or decrypt another message? (yes/no): ")
            if loop_terminate.lower() == "yes":
                continue
            elif loop_terminate.lower() == "y":
                continue
            else:
                print("Thanks for using the program, goodbye!")
                break

    enter_message()
main()