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
        new_client = Client(ID, name) #?надо ли создавать объет для хранения счетов
        self.clients[ID] = name
        self.number_of_clients += 1
        pass

    def find_client(self, ID):
        for client in self.clients:
            if ID in client:
                return True
        return False
        pass

class BankInterface:
    def __init__(self, bank):
        self._bank = bank

    
    #// MAIN_menu вроде готово
    def MAIN_menu (self, bank): #*def to create or sing in ID 
        while True:

            action = int(input("Choose action:\n 1.Sing in to ID.\n 2.Create ID"))
            match action:
                case 1:
                    self.sign_in(bank) #дальнейший ход интерфейса
                    return
                case 2:
                    self.registration(bank) #дальнейший ход интерфейса
                    return
                case _:
                    print("Invalid option. Try again.")

    #//тут вроже тоже всё
    def sign_in(self, bank): 
        while True:
            client_ID = int(input("Enter ID: ")) #?потом string
            if bank.find_id(client_ID):
                #дальнейший интерфейс
                return
            else:
                print("No valid ID. Try again or create an ID.")
                
                while True:
                    action = int(input("1.Try again\n 2.Create new ID"))
                    match action:
                        case 1:
                            break #back to first cycle
                        case 2:
                            self.registration(bank)
                            #?return или сразу переход на (3)
                        case _:
                            print("Invalid option. Try again.")

    def registration(bank):
        client_name = input("Enter your name and surname: ")
        bank.add_client(client_name)
        
class ClientInterface:

    def MAIN_not_menu(self, client):
        while True:

            action = int(input("Choose action:\n 1.Open account.\n 2.Close account.\n 3.Operations with account."))
            match action:
                        case 1:
                            client.open_account()
                            return 
                        case 2:
                            client.open_account()
                            return
                        case 3:
                            #next option
                            pass
                        case _:
                            print("Invalid option. Try again.")



    
    

class BankAccount:
    #TODO currency of accaount
    pass

class Client:


    def __init__(self, ID, name):
        self.ID = ID
        self.name = name

    def open_account(self):
        pass
    def close_account(self):
        pass
    def TopUp_account(self):
        pass
    def money_transfer(self):
        pass
    #TODO: polya: input_ID
    #TODO somehow make creation of new accounts
    pass