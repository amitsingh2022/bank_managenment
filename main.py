import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []
    
    try:
        if Path(database).exists():
            with open (database) as fs :
                data = json.loads(fs.read())
        else:
            print("No such file exist")
    except Exception as err:
        print(f"An Exception occered as {err}")

    @classmethod
    def __update(cls):
        with open (cls.database, 'w') as fs: 
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return"".join(id)



    def createaccount(self):
        info = {
            "name": input("Tell your name:-"),
            "age": int(input("Tell your age:-")),
            "email": input("Tell your email:-"),
            "pin": int(input("Tell your 4 digit pin:-")),
            "accountNo.":Bank.__accountgenerate(),
            "balance":0
        }
        if info['age']< 18 or len(str(info['pin'])) != 4:
            print("Sorry you cannot create your account")
        else:
            print("Account has been created sucessfully")
            for i in info:
                print(f"{i}:{info[i]}")
            print ("Please note down your account number")

            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("Please enter your account number:-")
        pin = int(input ("Please tell your pin as well:-"))  

        userdata = [i for i in Bank.data if i['accountNo.']== accnumber and i['pin']==pin]

        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("How much money you wnat to deposit:-"))
            if amount > 500000 or amount<0:
                print ("Sorry the amount is too much. You can deposit below 500000")

            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited Sucessfully")
    
    def withdrawmoney(self):
        accnumber = input("Please enter your account number:-")
        pin = int(input ("Please tell your pin as well:-"))  

        userdata = [i for i in Bank.data if i['accountNo.']== accnumber and i['pin']==pin]

        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("How much money you wnat to withdraw:-"))
            if userdata[0]['balance'] < amount:
                print ("Sorry the amount is insufficient.")

            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrawn Sucessfully")

    def showdetails(self):
        accnumber = input("Please enter your account number:-")
        pin = int(input ("Please tell your pin as well:-"))

        userdata = [i for i in Bank.data if i['accountNo.']== accnumber and i['pin']==pin]
        print ("Your Information are \n\n\n")
        for i in userdata[0]:
            print(f"{i}:{userdata[0][i]}")
        
    def updatedetails(self):
        accnumber = input("Please enter your account number:-")
        pin = int(input ("Please tell your pin as well:-"))

        userdata = [i for i in Bank.data if i['accountNo.']== accnumber and i['pin']==pin]

        if userdata == False:
            print("no such user found")
        else:
            print ("You cannot change the age, account number, balance")
            print ("Fill the details for change or leave it empty if no change ")

            newdata = {
                "name": input("Please enter new name or press enter:-"),
                "email": input("Please tell your new email or enter to skip:-"),
                "pin": input("Please enter your new pin or enter to skip:-")
            }

            if newdata["name"] == "":
                newdata ["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata ["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata ["pin"] = userdata[0]["pin"]

            newdata['age'] = userdata[0]['age']
            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata [0]['balance']

            if type(newdata['pin'])== str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i]= newdata[i]
            
            Bank.__update()
            print ("Details updated successfully")

user = Bank()
print("Press 1 for creating an account")
print ("Press 2 for depositing money in the account")
print ("Press 3 for withdrawing money from account")
print ("Press 4 for details")
print ("Press 5 for updating the details")
print ("Press 6 for deleting the account")

check = int(input("tell your response:-"))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()


