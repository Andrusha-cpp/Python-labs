#! 
class CafeError(Exception): 
    pass

class CoffeeChooseError(CafeError):
    def __init__(self, option):
        message = f"Invalid coffee position. It must be from 1 to 7. You choose: {option}"
        super().__init__(message)

class VolumeChooseError(CafeError):
    def __init__(self, option):
        message = f"Invalid coffee volume. Choose from the options."
        super().__init__(message)

class ContinueChooseError(CafeError):
    def __init__(self):
        message = "Invalid option. It must be Yes or No."
        super().__init__(message)


class Coffee:
    def __init__(self, price):
        self.price = price

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
        return self.price[100]

class Double_Espresso(Coffee):
    def __init__(self, price = {200: 3.5}):
        self.price = price
    def get_price(self):
        return self.price[200]
############################################################################################
class Cafe:
    latte = Latte()
    capuchino = Capuchino()
    espresso = Espresso()
    double_espresso = Double_Espresso()
    flat_white = Flat_white()
    american = American()
    raf = Raf()
    check = {}

    def __init__(self):
        latte = Latte()
        capuchino = Capuchino()
        espresso = Espresso()
        double_espresso = Double_Espresso()
        flat_white = Flat_white()
        american = American()
        raf = Raf()
        check = {}

    def find_price(self, kind, volume):
        match kind:
            case 1:
                prices = self.latte.get_price()
                price = prices[volume]
            case 2:
                prices = self.capuchino.get_price()
                price = prices[volume]
            case 3:
                price = self.espresso.get_price()
            case 4:
                price = self.double_espresso.get_price()
            case 5:
                prices = self.flat_white.get_price()
                price = prices[volume]
            case 6:
                prices = self.american.get_price()
                price = prices[volume]
            case 7:
                prices = self.raf.get_price()
                price = prices[volume]
        return price
    
    def check_creation(self):
        coffees = {1: "Latte", 2: "Cappuchino", 3: "Espresso", 4: "Double Espresso", 5: "Flat White", 6: "Americano", 7: "Raf"}
        total_price = 0
        print("\n" + "=" * 30)
        print("Check".center(30))
        print("=" * 30)

        n = 1
        for kind, volume in self.check.items():
            total_price += self.find_price(kind, volume)
            if kind == 3 or kind == 4:
                print(f"{n}. {coffees[kind]}")
            else:
                print(f"{n}. {coffees[kind]} - {volume}ml")
            n += 1

        print("=" * 30)
        print(f"TOTAL PRICE: {total_price}BYN")
        print("=" * 30)

    def add_to_check(self, kind, volume):
        self.check[kind] = volume

############################################################################################

class Interface:
    def Choose_volume(self, coffee_kind):
        if coffee_kind in [1, 2]:
            prices = {1: 250, 2: 350, 3: 450}
            print("1. 250ml (3.5 BYN)\n2. 350ml (4.5 BYN)\n3. 450ml (5.5 BYN)")
            choice = int(input("Choose volume: "))
            if choice not in prices:
                raise VolumeChooseError
            else:
                return prices[choice]
        elif coffee_kind in [5, 6, 7]:
            print("1. 250ml (3.5 BYN)\n2. 350ml (4.5 BYN)")
            prices = {1: 250, 2: 350, 3: 450}
            choice = int(input("Choose volume: "))
            if choice not in prices:
                raise VolumeChooseError
            else:
                return prices[choice]
        elif coffee_kind == 6:
            return 100
        elif coffee_kind == 7:
            return 200

    @staticmethod
    def Choose_coffee():
        print("\n", "=" * 30)
        print("MENU".center(30))
        print("=" * 30)
        print("""1. Latte (3.5-5.5 BYN)
2. Capuchino (3.5-5.5 BYN)
3. Espresso (2 BYN)
4. Double Espresso (3.5 BYN)
5. Flat White (3.5-4.5 BYN)
6. American (3.5-4.5 BYN)
7. Raf (3.5-4.5 BYN)""")
        print("=" * 30)
        choice = int(input("Choose coffee you'd like to order:"))

        if choice not in range(1, 8):
            raise CoffeeChooseError(choice)
        return choice
    
    def Main_Interface(self):
        cafe = Cafe()
        while(True):
            kind = self.Choose_coffee()
            volume = self.Choose_volume(kind)
            cafe.add_to_check(kind, volume)
            continue_ = input("Do you want to order anything else? (Yes/No):")
            print(continue_)
            
            if continue_ in ['YES', 'yes', 'Yes', 'ofcourse', 'yeap', ' yes']:
                continue
            elif continue_ in ['No', 'no', 'NO']:
                break
            else: 
                raise ContinueChooseError
        cafe.check_creation()

##################################################################################################        
def main():
    interf = Interface()
    interf.Main_Interface()

main()