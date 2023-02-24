"""Code by : Ganesh Parajuli student id = 2331188"""
"""The program is about Caesar Cipher """
def main():
    """ method ko barema"""
    #created universal variable.
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    def welcome(): # Function is created.
        print("Welcome to Caesar Cipher")
        print("This program encrypts and decrypts text with the Caesar Cipher.")
    def enter_message(): #This function is created to take decision and message.
        user_input=input("Would you like to encrypt(press 'e') or decrypt(press 'd')?")
        if user_input=='E' or user_input=='e' :#Condition is created.
            user_message=input("Enter your message here: ")
            while True:
                if user_message.isnumeric()==False:
                    user_message=user_message.upper()        #converting messages into upper case
                    break
                else:
                    print("Only strings please")
                    user_message=input("Enter another message here: ")
            try:
                shift_value=int(input("Enter the shift value"))
            except:
                print("Please enter interger value")
                enter_message()
            encrypt(user_message,shift_value) #function is called.
        elif user_input=='D' or user_input=='d' :#Else condition is created.
            user_message=input("Enter your message here:")
            while True:
                if user_message.isnumeric()==False:
                    user_message=user_message.upper()        #converting messages into upper case
                    break
                else:
                    print("Only strings please")
                    user_message=input("Enter another message here: ")
            user_message=user_message.upper()
            try:
                shift_value=int(input("Enter the shift value"))
            except:
                print("Please enter interger value")
                enter_message()
            decrypt(user_message,shift_value)
        else:
            print("Value is worng you should enter valid value. Do you wanna continue?")
            choose1=input("Enter Y for yes and N for no.")
            if choose1=='Y' or choose1=='y':
                enter_message() #function calling to continue
            else:
                print("Program is end")

    def encrypt(user_message,shift_value):
        encrypted_message=""
        for i in user_message:
            if i == " " :
                encrypted_message += " "
            else:
                #Here we use i because we need to find cipher value for every word
                #(it will return the value from aplphabet using indexing method)
                place=shift_value+alphabet.index(i)
                #used mord function to restart counting after value end.
                place%=26
                encrypted_message+=alphabet[place]
                #Replace word that should be replaced
        print("Encrypted is completd..")
        print("Encrypted value are: ",encrypted_message)
        ending()

    def decrypt(user_message,shift_value):  #Same as encryption but opposite or comes from last.
                                            #going back to original places
        decrypted_message=""
        for i in user_message:
            if i== " ":
                decrypted_message += " "
            else:
                place=alphabet.index(i)-shift_value
                place%=26
                decrypted_message+=alphabet[place]
        print("Decrypted is completd..")
        print("Decrypted value are: ",decrypted_message)
        ending()
    def ending(): #Creating final part
        print("Do you want to continue more? ")
        choose3=input("Press Y for continue and N for end of program")
        if choose3=='Y' or choose3=='y':
            enter_message()
        elif choose3=='N' or choose3=='n':
            print("Program is end")
        else:
            print("You pressed wrong value even programmed is end")
    welcome()
    enter_message()
main()
