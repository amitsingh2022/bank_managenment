import json
import random
import string
from pathlib import Path

class Bank:
    def createaccount(self):
        pass



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