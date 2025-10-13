class Bank:

    def __init__(self, name):
        self.clients = {}
        self.number_of_clients = 0
        self.bank_name = name

    def add_client(self, name):
        ID = 10000000 + self.number_of_clients + 1
        self.clients[ID] = Client(ID, name)
        self.number_of_clients += 1
        return ID

    def find_client(self, ID):
        return ID in self.clients
    
    def get_client(self, ID):
        return self.clients[ID]

class Client:

    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.accounts = {}
        self.number_of_accounts = 0

    def get_account(self, acc_number):
        return self.accounts.get(acc_number)
 
    def get_ID(self):
        return self.ID

    def find_account(self, acc_number):
        return acc_number in self.accounts

    def open_account(self, currency):
        account_number = f"{self.number_of_accounts + 1:02d}C{self.ID}" #number 00C00000000 
        self.accounts[account_number] = BankAccount(currency, self.ID, account_number)
        self.number_of_accounts += 1
        return account_number
        
    def close_account(self, acc_number):
        del self.accounts[acc_number]
        print("Account succesfully deleted.")
        pass

    def account_statement(self):
        if not self.accounts:
            print("You have no открытых счетов.")
            return

        with open(f"statement_{self.ID}.txt", "a") as f:  # просто добавление в файл
            f.write(f"\nAccount Statement for {self.name} (ID: {self.ID})\n")
            for acc in self.accounts.values():
                f.write(f"{acc.account_number}: {acc.currency}, balance = {acc.balance}\n")

        print(f"Statement updated in 'statement_{self.ID}.txt'")

class BankAccount:

    def __init__(self, currency, owner_ID, account_number):
        self.currency = currency
        self.owner_ID = owner_ID
        self.balance = 0
        self.account_number = account_number

    def TopUp_account(self, add_balance):
        self.balance += add_balance

    def money_transfer(self, acc_recipient, add_balance):
        self.withdraw_money(add_balance)
        acc_recipient.TopUp_account(add_balance)
        print(f"Transferred {add_balance} {self.currency} to account {acc_recipient.account_number}.")

    def withdraw_money(self, take_balance):
        self.balance -= take_balance
        pass

    def get_balance(self):
        return self.balance

class BankInterface:
    def __init__(self, bank):
        self.bank = bank

    def MAIN_menu (self): #*def to create or sing in ID 
        while True:

            action = int(input("Choose action:\n 1.Sing in to ID.\n 2.Create new ID.\n 3.Exit menu.\n"))
            match action:
                case 1:
                    self.sign_in() #дальнейший ход интерфейса внутри
                    return
                case 2:
                    self.registration() #дальнейший ход интерфейса внутри
                    return
                case 3:
                    return
                case _:
                    print("Invalid option. Try again.")

    def sign_in(self): 
        while True:
            client_ID = int(input("Enter ID: ")) 

            if self.bank.find_client(client_ID):
                client_interface = ClientInterface(self.bank.get_client(client_ID)) #go to user interface
                client_interface.MAIN_not_menu()
                return
            else:
                print("No valid ID. Try again or create an ID.")
                
                while True:
                    action = int(input("1.Try again\n 2.Create new ID\n"))
                    match action:
                        case 1:
                            break #back to first cycle
                        case 2:
                            self.registration()
                            return
                        case _:
                            print("Invalid option. Try again.")

    def registration(self):
        client_name = input("Enter your name and surname: ")

        client_ID = self.bank.add_client(client_name)
        print(f"You've been succesfully registrated! Your ID: {client_ID}")
        client_interface = ClientInterface(self.bank.get_client(client_ID))
        client_interface.MAIN_not_menu()  #go to user interface

        
class ClientInterface:

    def __init__(self, client):
        self.client = client

    def MAIN_not_menu(self):
        while True:

            action = int(input("Choose action:\n 1.Open account.\n 2.Close account." \
            "\n 3.Operations with account.\n 4.Get all accounts statement\n 5.Exit menu.\n"))
            match action:
                        case 1:
                            self.openning_interface()
                            print("Account succesfully opened.")
                        case 2:
                            self.clossing_interface()
                            print("Account closed.")
                        case 3:
                            self.operations_interface()
                        case 4:
                            self.client.account_statement()
                        case 5:
                            return
                        case _:
                            print("Invalid option. Try again.")

    def openning_interface(self):
        while True:

            action = int(input("Choose currency of account:\n 1.USD.\n 2.BYN.\n 3.EUR.\n"))
            match action:
                        case 1:
                            print(f"Your account number {self.client.open_account("USD")}")
                            return 
                        case 2:
                            print(f"Your account number {self.client.open_account("BYN")}")
                            return
                        case 3:
                            print(f"Your account number {self.client.open_account("EUR")}")
                            return
                        case _:
                            print("Invalid option. Try again.")

    def clossing_interface(self):
        while True:
            acc_number = input("Enter account number: ") #makedecorator
            if self.client.find_account(acc_number):

                while True:
                    action = int(input("Are you sure you want close this account?\n" \
                                       "1.Yes\n 2.No\n"))
                    match action:
                        case 1:
                            self.client.close_account(acc_number)
                            return
                        case 2:
                            return
                        case _:
                            print("Invalid option. Try again.")

            else:
                print("You don't have account with this number. Try again.")

    def operations_interface(self):
        acc_number = input("Enter account number: ").strip()
        if not self.client.find_account(acc_number):
            print("No such account.")
            return

        account = self.client.get_account(acc_number)
        acc_interface = AccountInterface(account, self.client)
        acc_interface.account_operations()

class AccountInterface:

    def __init__(self, account, client):
        self.account = account
        self.client = client

    def account_operations(self):
        while True:

            action = int(input("Choose action:\n 1.Top up account.\n 2.Withdraw money.\n 3.Transfer money to account.\n 4.Exit."))
            match action:
                        case 1:
                            self.TopUp()
                        case 2:
                            self.withdraw()
                        case 3:
                            self.transfer()
                        case 4:
                            return
                        case _:
                            print("Invalid option. Try again.")


    def TopUp(self):
        try:
            amount = float(input("Enter amount to top up: "))
            if amount <= 0:
                print("Amount must be positive.")
                return
            self.account.TopUp_account(amount)
            print(f"Account topped up. New balance: {self.account.balance}")
        except ValueError:
            print("Invalid input.")


    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Amount must be positive.")
                return
            if self.account.balance >= amount:
                self.account.withdraw_money(amount)
                print(f"Withdraw successful. New balance: {self.account.balance}")
            else:
                print("Not enough money.")
        except ValueError:
            print("Invalid input.")
            

    def transfer(self):
        while True:
            acc2_number = input("Enter number of account recipient: ")
            if self.client.find_account(acc2_number):
                recipient_account = self.client.get_account(acc2_number)  # get account
                while True:
                    try:
                        add_balance = float(input("Enter amount of money to transfer: "))
                        if add_balance <= 0:
                            print("Amount must be positive.")
                            continue
                        if self.account.balance < add_balance:
                            print("Not enough funds for transfer.")
                            continue
                        self.account.money_transfer(recipient_account, add_balance)  
                        return
                    except ValueError:
                        print("Invalid input.")
            else:
                print("You don't have account with this number. Try again.")


def main():
    AlphaBank = Bank("AlphaBank")
    interface = BankInterface(AlphaBank)

    interface.MAIN_menu()
    pass

main()