############################################################################################
from abc import abstractmethod

class Coffee:

    def __init__(self, price):
        self.price = price

    @abstractmethod
    def get_price(self):
        return self.price


class Latte(Coffee):
    def __init__(self, price = {250: 3.5, 350: 4.5, 450: 5.5}):
        self.price = price
    def get_price(self):
        return self.price

class Capuchino(Coffee):
    def __init__(self, price = {250: 3.5, 350: 4.5, 450: 5.5}):
        self.price = price
    def get_price(self):
        return self.price

class American(Coffee):
    def __init__(self, price = {250: 3.5, 350: 4.5}):
        self.price = price
    def get_price(self):
        return self.price

class Raf(Coffee):
    def __init__(self, price = {250: 3.5, 350: 4.5}):
        self.price = price
    def get_price(self):
        return self.price

class Flat_white(Coffee):
    def __init__(self, price = {250: 3.5, 350: 4.5}):
        self.price = price
    def get_price(self):
        return self.price
    
class Espresso(Coffee):
    def __init__(self, price = {100: 2}):
        self.price = price
    def get_price(self):
        return self.price

class Double_Espresso(Coffee):
    def __init__(self, price = {200: 3.5}):
        self.price = price
    def get_price(self):
        return self.price
############################################################################################
class Cafe:
    def __init__(self):
        latte = Latte()
        capuchino = Capuchino()
        espresso = Espresso()
        double_espresso = Double_Espresso()
        flat_white = Flat_white()
        american = American()
        raf = Raf()
        Check = {}

    def find_price(self, kind, volume):
        match kind:
            case 1:
                prices = self.latte.get_price()
                price = prices[volume]
            case 2:
                prices = self.capuchino.get_price()
                price = prices[volume]
            case 3:
                prices = self.espresso.get_price()
                price = prices[volume]
            case 4:
                prices = self.double_espresso.get_price()
                price = prices[volume]
            case 5:
                prices = self.flat_white.get_price()
                price = prices[volume]
            case 6:
                prices = self.american.get_price()
            case 7:
                prices = self.raf.get_price()

        return price

############################################################################################

class Interface:
    def Choose_volume(coffee_kind):
        if coffee_kind in [1, 2]:
            prices = {1: 250, 2: 350, 3: 450}
            print("1. 250ml\n2. 350ml\n 3. 450ml")
            choice = int(input("Choose volume: "))
            return prices[choice]
        elif coffee_kind in [3, 4, 5]:
            print("1. 250ml\n2. 350ml")
            prices = {1: 250, 2: 350, 3: 450}
            choice = int(input("Choose volume: "))
            return prices[choice]
        elif coffee_kind == 6:
            return 100
        elif coffee_kind == 7:
            return 200

    @staticmethod
    def Choose_coffee():
        print("""1. Latte
2. Capuchino
3. Espresso
4. Double Espresso
5. Flat White
6. American
7. Raf
""")
        #TODO exception
        choice = int(input("Choose coffee you'd like to order:"))
        return choice
    
    def Main_Interface(self):
        cafe = Cafe()
        kind = self.Choose_coffee()
        volume = self.Choose_volume()
        cafe.add_to_check(kind, volume)




##################################################################################################        
def main():
    interf = Interface()
    interf.Make_order()

main()