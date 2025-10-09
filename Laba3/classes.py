class Bank:
    clients = {}
    number_of_clients = 0

    def __init__(self, name):
        self.clients = {}
        self.number_of_clients = 0
        self.bank_name = name
        pass

    def add_client(self, ID, name):
        ID = self.number_of_clients #TODO реализоаать ID
        new_client = Client(ID, name) #?надо?
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

    def Sign_in_ID(bank): #*def to create or sing in ID
        while True:

            action = input("Choose action:\n 1.Sing in to ID.\n 2.Create ID")
            match action:
                case 1:
                    self.sign_in(bank)
                    pass
                case 2:

                    pass
                case _:
                    print("Invalid option. Try again.")

    def sign_in(bank): 
        while True:
            ID = input("Enter ID: ")
            if bank.find_id():
                #continue 
            else:
                print("No valid ID. Try again or create an ID.")
                
                while True:
                    action = input("1.Try again\n 2.Create new ID")
                    match action:
                        case 1:
                            break
                        case 2:
                            self.registration(bank)
                            #?return
                        case _:
                            print("Invalid option. Try again.")

    def registration(bank):
        client_name = input("Enter your name and surname: ")
        bank.add_client()
        




    
    

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