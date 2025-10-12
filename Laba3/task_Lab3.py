from classes import Bank, BankAccount, Client, BankInterface, ClientInterface


def main():
    AlphaBank = Bank("AlphaBank")
    interface = BankInterface(AlphaBank)

    interface.MAIN_menu()
    pass

main()