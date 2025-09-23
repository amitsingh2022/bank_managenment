import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path (database).exists():
            with open (database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exist")
    except Exception as err:
        print(f"An Exception occered as {err}")

    @staticmethod
    def update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))


    def createaccount(self):
        info = {
            "name":input ("Tell your name:-"),
            "age": int(input("Tell Your age:-")),
            "email":input("Tell your email:-"),
            "pin":int(input("Tell your pin:-")),
            "accountNo.": 1234,
            "balance": 0
        }
        if info['age'] < 18 or len(str(info['pin'])) !=4:
            print ("Sorry you cannot create your account.")
        else:
            print("Your account has been created successfully.")
            for i in info:
                print (f"{i}:{info[i]}")
            print ("Please note down your account number.")

            Bank.data.append(info)
            Bank.update() 


user = Bank()




print("Press 1 for creating an account")
print("Press 2 for depositing the money in the bank")
print("Press 3 for withdrawing the money from the bank")
print("Press 4 for checking the details of the account")
print("Press 5 for updating the details of the account")
print ("Press 6 fro deleting the account")

check = int(input("Tell your response:-"))

if check == 1:
    user.createaccount()