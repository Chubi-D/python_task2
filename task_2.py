#importing strings and random

import string
import random
Users = []
def generateRandomPassword(firstName, lastName):
    all_string = string.ascii_lowercase+string.ascii_uppercase+string.punctuation+string.digits
    random_string = ''.join(random.choice(all_string) for i in range(5))
    random_password = firstName[0:2]+lastName[-2:0]+random_string
    return random_password

def addUser(first, last, email, password):
    Users.append([first, last, email, password])

def printUserDetails():
    output= ''
    for i in range(len(Users)):
        user= Users[i]
        output +='User {}:\n'.format(i+1)
        output += 'First name - {}:\n'.format(user[0])
        output += 'Last name - {}\n'.format(user[1])
        output += 'Email -{}\n'.format(user[2])
        output += 'Password -{}\n\n'.format(user[3])
        print(output)

def main():
    first_name = input('Enter your First Name ')
    last_name = input('Enter your Last Name ')
    emai = input('Enter your Email Address ')
    password = generateRandomPassword(first_name, last_name)
    ask = input('Are you okay with the password: {} (yes/no)? '.format(password))
    if ask.lower() =='no':
        password = ''
        while len(password) < 7:
            password = input('Input new password ')
            addUser(first_name, last_name, emai, password)
anotherUser = True
while anotherUser:
    main()
    question= input('Would you like to input another User? (yes/no)? ')
    if question.lower()== 'no':
        anotherUser= False
        printUserDetails()





