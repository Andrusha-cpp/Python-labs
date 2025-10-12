class Bank:

    def __init__(self, name):
        self.clients = {}
        self.number_of_clients = 0
        self.bank_name = name

    def add_client(self, name):
        ID = self.number_of_clients #TODO реализоаать ID
        self.clients[ID] = Client(ID, name)
        self.number_of_clients += 1
        return ID

    def find_client(self, ID):
        return ID in self.clients
    
    def get_client(self, ID):
        return self.clients[ID]

class BankInterface:
    def __init__(self, bank):
        self.bank = bank

    #// MAIN_menu вроде готово
    def MAIN_menu (self): #*def to create or sing in ID 
        while True:

            action = int(input("Choose action:\n 1.Sing in to ID.\n 2.Create new ID.\n"))
            match action:
                case 1:
                    self.sign_in() #дальнейший ход интерфейса внутри
                    return
                case 2:
                    self.registration() #дальнейший ход интерфейса внутри
                    return
                case _:
                    print("Invalid option. Try again.")

    #//тут вроде тоже всё
    def sign_in(self): 
        while True:
            client_ID = int(input("Enter ID: ")) #?потом string
            if self.bank.find_id(client_ID):
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
            "\n 3.Operations with account.\n 4.Get all accounts statement\n"))
            match action:
                        case 1:
                            self.openning_interface()
                            print("Account succesfully opened.")
                            return 
                        case 2:
                            self.clossing_interface()
                            print("Account closed.")
                            return
                        case 3:
                            while True:
                                acc_number = input("Enter account number: ")
                                if self.client.find_account(acc_number):
                                    acc_interface = AccountInterface(acc_number)
                                    acc_interface.account_operations()
                                    return
                                else:
                                    print("You don't have account with this number. Try again.")
                        case 4:
                            self.client.accounts_statement()
                            print("Something")
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


class AccountInterface:

    def __init__(self, account):
        self.account = account

    def account_operations(self):
        while True:

            action = int(input("Choose action:\n 1.Top up account.\n 2.Withdraw money.\n 3.Transfer money to account.\n"))
            match action:
                        case 1:
                            self.account.TopUp_account()
                            return 
                        case 2:
                            self.account.withdraw_money()
                            return
                        case 3:
                            self.account.money_transfer()
                            return
                        case _:
                            print("Invalid option. Try again.")



    
class BankAccount:

    def __init__(self, currency, owner_ID, account_number):
        self.currency = currency
        self.owner_ID = owner_ID
        self.balance = 0
        self.account_number = account_number

    def TopUp_account(self):
        pass
    def money_transfer(self):
        pass
    def withdraw_money(self):
        pass




class Client:

    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.accounts = {}
        self.number_of_accounts = 0

    def get_ID(self):
        return self.ID

    def find_account(self, acc_number):
        return acc_number in self.accounts

    #? get_name
    def open_account(self, currency):
        self.accounts[self.number_of_accounts] = BankAccount(currency, self.ID, self.number_of_accounts)
        self.number_of_accounts += 1
        return self.number_of_accounts - 1
        
    def close_account(self, acc_number):
        del self.accounts[acc_number]
        print("Account succesfully deleted.")
        pass

    def account_statement(self):
        pass
    