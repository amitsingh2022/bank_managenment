import json
import random
import string
from pathlib import Path
import streamlit as st

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                data = json.load(fs)
        else:
            data = []
    except Exception as err:
        st.error(f"An error occurred: {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        acc_id = alpha + num + spchar
        random.shuffle(acc_id)
        return "".join(acc_id)

    @classmethod
    def find_user(cls, accnumber, pin):
        return [i for i in cls.data if i['accountNo.'] == accnumber and i['pin'] == pin]

    def createaccount(self, name, age, email, pin):
        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0
        }
        if age < 18 or len(str(pin)) != 4:
            return None
        Bank.data.append(info)
        Bank.__update()
        return info

    def depositmoney(self, accnumber, pin, amount):
        userdata = Bank.find_user(accnumber, pin)
        if not userdata:
            return "User not found"
        if amount > 500000 or amount < 0:
            return "Invalid deposit amount"
        userdata[0]['balance'] += amount
        Bank.__update()
        return "Deposit successful"

    def withdrawmoney(self, accnumber, pin, amount):
        userdata = Bank.find_user(accnumber, pin)
        if not userdata:
            return "User not found"
        if userdata[0]['balance'] < amount:
            return "Insufficient balance"
        userdata[0]['balance'] -= amount
        Bank.__update()
        return "Withdrawal successful"

    def showdetails(self, accnumber, pin):
        userdata = Bank.find_user(accnumber, pin)
        if not userdata:
            return None
        return userdata[0]

    def updatedetails(self, accnumber, pin, name=None, email=None, newpin=None):
        userdata = Bank.find_user(accnumber, pin)
        if not userdata:
            return "User not found"

        if name:
            userdata[0]['name'] = name
        if email:
            userdata[0]['email'] = email
        if newpin:
            userdata[0]['pin'] = newpin

        Bank.__update()
        return "Details updated successfully"

    def delete(self, accnumber, pin):
        userdata = Bank.find_user(accnumber, pin)
        if not userdata:
            return "User not found"
        Bank.data.remove(userdata[0])
        Bank.__update()
        return "Account deleted successfully"


# ---------------- STREAMLIT APP ----------------
st.title("🏦 Simple Bank System")

menu = st.sidebar.radio("Menu", ["Create Account", "Deposit", "Withdraw", "Show Details", "Update Details", "Delete Account"])

bank = Bank()

if menu == "Create Account":
    st.subheader("Create a New Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, step=1)
    email = st.text_input("Email")
    pin = st.number_input("4-digit PIN", min_value=1000, max_value=9999, step=1)
    if st.button("Create"):
        info = bank.createaccount(name, age, email, pin)
        if info:
            st.success("Account created successfully!")
            st.write(info)
        else:
            st.error("You must be 18+ and PIN should be 4 digits.")

elif menu == "Deposit":
    st.subheader("Deposit Money")
    acc = st.text_input("Account Number")
    pin = st.number_input("PIN", min_value=1000, max_value=9999, step=1)
    amount = st.number_input("Amount", min_value=0, step=100)
    if st.button("Deposit"):
        result = bank.depositmoney(acc, pin, amount)
        st.write(result)

elif menu == "Withdraw":
    st.subheader("Withdraw Money")
    acc = st.text_input("Account Number")
    pin = st.number_input("PIN", min_value=1000, max_value=9999, step=1)
    amount = st.number_input("Amount", min_value=0, step=100)
    if st.button("Withdraw"):
        result = bank.withdrawmoney(acc, pin, amount)
        st.write(result)

elif menu == "Show Details":
    st.subheader("Account Details")
    acc = st.text_input("Account Number")
    pin = st.number_input("PIN", min_value=1000, max_value=9999, step=1)
    if st.button("Show"):
        details = bank.showdetails(acc, pin)
        if details:
            st.json(details)
        else:
            st.error("No account found")

elif menu == "Update Details":
    st.subheader("Update Account Details")
    acc = st.text_input("Account Number")
    pin = st.number_input("Old PIN", min_value=1000, max_value=9999, step=1)
    new_name = st.text_input("New Name (optional)")
    new_email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)")
    if st.button("Update"):
        result = bank.updatedetails(acc, pin, new_name, new_email, int(new_pin) if new_pin else None)
        st.write(result)

elif menu == "Delete Account":
    st.subheader("Delete Account")
    acc = st.text_input("Account Number")
    pin = st.number_input("PIN", min_value=1000, max_value=9999, step=1)
    if st.button("Delete"):
        result = bank.delete(acc, pin)
        st.write(result)
