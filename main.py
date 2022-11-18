import csv
import pandas as pd
import os


class Wallet:
    all = []

    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount
        Wallet.all.append((self.name, self.amount))

    @staticmethod
    def create_wallet(name, init_amount):
        Wallet(name, init_amount)

    @classmethod
    def wallet_display(cls):
        df = pd.read_csv('wallets.csv')
        if df.empty:
            print("no wallets registerd")
        else:
            print(df.to_string())
            return df

    # checks if csv file is empty to init with headers
    @classmethod
    def init_database(cls):
        header = ["name", "amount"]
        if os.stat("wallets.csv").st_size == 0:
            with open('wallets.csv', 'w') as f:
                writer = csv.writer(f)
                writer.writerow(header)

    # appends wallets to csv file
    @classmethod
    def add_to_database(cls):
        t_list = list(cls.all[-1])
        print(t_list)
        data = t_list
        with open('wallets.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data)

    @classmethod
    def add_amount(cls, index, amount = 0):
        df = pd.read_csv('wallets.csv')
        df.loc[index, 'amount'] = int(df.loc[index, 'amount']) + amount  # type: ignore
        df.to_csv('wallets.csv', index = False)
        print(df.to_string())

    @classmethod
    def subtract_amount(cls, index, amount = 0):
        df = pd.read_csv('wallets.csv')
        df.loc[index, 'amount'] = int(df.loc[index, 'amount']) - amount  # type: ignore
        df.to_csv('wallets.csv', index = False)
        print(df.to_string())


# starts the app 
def start_app():
    value = input("""
    Press 1 to create a wallet
    Press 2 to display the existing wallets
    Press 3 to add money to your wallet
    Press 4 to subtract money from your wallet
    Press q to quit
    """)
    Wallet.init_database()
    while value != "q":
        if value == "1":
            name = input("Please enter the wallet name: ")
            init_amount = int(input("Please enter the initial wallet amount: "))
            Wallet.init_database()
            Wallet.create_wallet(name, init_amount)
            Wallet.add_to_database()
            value = input("""
            Press 1 to create a wallet
            Press 2 to display the existing wallets
            Press 3 to add money to your wallet
            Press 4 to subtract money from your wallet
            Press q to quit
            """)

        elif value == "2":
            df = pd.read_csv('wallets.csv')

            if df.empty:
                print("no wallets registerd")
                value = input("""
            Press 1 to create a wallet
            Press 2 to display the existing wallets
            Press 3 to add money to your wallet
            Press 4 to subtract money from your wallet
            Press q to quit
            """)
            else:
                Wallet.wallet_display()
                value = input("""
            Press 1 to create a wallet
            Press 2 to display the existing wallets
            Press 3 to add money to your wallet
            Press 4 to subtract money from your wallet
            Press q to quit
            """)

        elif value == "3":
            Wallet.wallet_display()
            index = int(input("enter the index of the wallet you want to modify: "))
            amount = int(input("how much do you want to add? "))
            Wallet.add_amount(index, amount)
            value = input("""
            Press 1 to create a wallet
            Press 2 to display the existing wallets
            Press 3 to add money to your wallet
            Press 4 to subtract money from your wallet
            Press q to quit
            """)

        elif value == "4":
            Wallet.wallet_display()
            index = int(input("enter the index of the wallet you want to modify: "))
            amount = int(input("how much did you spend? "))
            Wallet.subtract_amount(index, amount)
            value = input("""
            Press 1 to create a wallet
            Press 2 to display the existing wallets
            Press 3 to add money to your wallet
            Press 4 to subtract money from your wallet
            Press q to quit
            """)

        else:
            value = input("Enter a valid input: ")


start_app()
