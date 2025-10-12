class Bank:
    clients = {}
    number_of_clients = 0

    def __init__(self, name):
        self.clients = {}
        self.number_of_clients = 0
        self.bank_name = name
        pass

    def add_client(self, name):
        ID = self.number_of_clients #TODO реализоаать ID
        self.clients[ID] = Client(ID, name)
        self.number_of_clients += 1
        pass

    def find_client(self, ID):
        for client in self.clients:
            if ID in client:
                return True
        return False

class BankInterface:
    def __init__(self, bank):
        self.bank = bank

    #// MAIN_menu вроде готово
    def MAIN_menu (self): #*def to create or sing in ID 
        while True:

            action = int(input("Choose action:\n 1.Sing in to ID.\n 2.Create ID\n"))
            match action:
                case 1:
                    self.sign_in(self.bank) #дальнейший ход интерфейса
                    return
                case 2:
                    self.registration(self.bank) #дальнейший ход интерфейса
                    return
                case _:
                    print("Invalid option. Try again.")

    #//тут вроде тоже всё
    def sign_in(self): 
        while True:
            client_ID = int(input("Enter ID: ")) #?потом string
            if self.bank.find_id(client_ID):
                #дальнейший интерфейс
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
                            print("You've been succesfully registrated!")
                            #?return или сразу переход на (3)
                        case _:
                            print("Invalid option. Try again.")

    def registration(self):
        client_name = input("Enter your name and surname: ")
        self.bank.add_client(client_name)
        
class ClientInterface:

    def __init__(self, client):
        self.client = client

    def MAIN_not_menu(self):
        while True:

            action = int(input("Choose action:\n 1.Open account.\n 2.Close account." \
            "\n 3.Operations with account.\n 4.Get all accounts statement\n"))
            match action:
                        case 1:
                            self.openning_interface(self.client)
                            print("Account succesfully opened.")
                            return 
                        case 2:
                            self.client.close_account()
                            print("Account closed.")
                            return
                        case 3:
                            self.account_operations(self.client)
                            return
                        case 4:
                            self.client.accounts_statement()
                            print("Something")
                            return
                        case _:
                            print("Invalid option. Try again.")

    def account_operations(self):
        while True:

            action = int(input("Choose action:\n 1.Top up account.\n 2.Withdraw money.\n 3.Transfer money to account.\n"))
            match action:
                        case 1:
                            self.client.TopUp_account()
                            return 
                        case 2:
                            self.client.withdraw_money()
                            return
                        case 3:
                            self.client.money_transfer()
                            return
                        case _:
                            print("Invalid option. Try again.")

    def openning_interface(self):
        while True:

            action = int(input("Choose currency of account:\n 1.USD.\n 2.BYN.\n 3.EUR.\n"))
            match action:
                        case 1:
                            self.client.open_account("USD")
                            return 
                        case 2:
                            self.client.open_account("BYN")
                            return
                        case 3:
                            self.client.open_account("EUR")
                            return
                        case _:
                            print("Invalid option. Try again.")


    
    

class BankAccount:
    amount_of_money = 0
    account_number = 0
    

    def __init__(self, currency, owner_ID):
        self.currency = currency
        self.owner_ID = owner_ID

    def TopUp_account(self):
        pass
    def money_transfer(self):
        pass
    def withdraw_money(self):
        pass




class Client:
    accounts = {}
    number_of_accounts = 0

    def __init__(self, ID, name):
        self.ID = ID
        self.name = name

    def get_ID(self):
        return self.ID

    #? get_name
    def open_account(self, currency):
        self.accounts[self.number_of_accounts] = BankAccount(currency, self.ID)
        self.number_of_accounts += 1
        
    def close_account(self):
        #delte from dict
        pass

    def account_statement(self):
        pass
    