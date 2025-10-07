class Bank:
    def __init__(self, name):
        self._clients = {}
        self._clients_number = 0
        self._bank_name = name
        pass

    def add_client():
        
        pass

    def find_client():
        pass

class BankInterface:
    def __init__(self, bank):
        self._bank = bank

    def Sign_in_ID(bank): #*def to create or sing in ID
        while True:

            action = input("Choose action:\n 1.Sing in to ID.\n 2.Create ID")
            match action:
                case 1:

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





    
    

class BankAccount:
    #TODO currency of accaount
    pass

class Client:
    def __init__(self, ID):
        self.ID = ID
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