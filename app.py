import streamlit as st

class BankApplication:
    bank_name = "SBI"

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return f"Transaction Successful. Collected {amount}"
        else:
            return "Insufficient Balance"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit Successful. Total Balance: {self.balance}"

    def update_mobile(self, new_number):
        self.mobile_number = new_number
        return f"Mobile number updated: {self.mobile_number}"

    def check_balance(self):
        return f"Total Account Balance: {self.balance}"


st.title("🏦 Bank Application")

# Session state to store account
if "account" not in st.session_state:
    st.session_state.account = None

menu = st.sidebar.selectbox(
    "Menu",
    ["Create Account", "Deposit", "Withdraw", "Check Balance", "Update Mobile"]
)

# Create Account
if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Name")
    account_number = st.text_input("Account Number")
    age = st.number_input("Age", min_value=1)
    mobile = st.text_input("Mobile Number")
    balance = st.number_input("Initial Balance", min_value=0)

    if st.button("Create"):
        st.session_state.account = BankApplication(
            name, account_number, age, mobile, balance
        )
        st.success("Account Created Successfully")

# Deposit
elif menu == "Deposit":
    st.subheader("Deposit Money")

    if st.session_state.account:
        amount = st.number_input("Enter Amount", min_value=1)

        if st.button("Deposit"):
            result = st.session_state.account.deposit(amount)
            st.success(result)
    else:
        st.warning("Please create account first")

# Withdraw
elif menu == "Withdraw":
    st.subheader("Withdraw Money")

    if st.session_state.account:
        amount = st.number_input("Enter Amount", min_value=1)

        if st.button("Withdraw"):
            result = st.session_state.account.withdraw(amount)
            st.success(result)
    else:
        st.warning("Please create account first")

# Check Balance
elif menu == "Check Balance":
    st.subheader("Check Balance")

    if st.session_state.account:
        result = st.session_state.account.check_balance()
        st.info(result)
    else:
        st.warning("Please create account first")

# Update Mobile
elif menu == "Update Mobile":
    st.subheader("Update Mobile Number")

    if st.session_state.account:
        new_number = st.text_input("New Mobile Number")

        if st.button("Update"):
            result = st.session_state.account.update_mobile(new_number)
            st.success(result)
    else:
        st.warning("Please create account first")



        