print("NAME:: RAYAN AHMED")
print("ROLL NO:: BITF20M535")

print("\n ***ASSIGNMENT CLASS (RESTAURANT MANAGEMENT SYSTEM)***\n")

class Restaurant:
    restaurantName = "&^~ AL-NAKHAL ARABIAN CUISINE (RDX FOODS) ~^&"

    def __init__(self, cName, cAdress, pNumber):
        self.cName = cName
        self.cAdress = cAdress
        self.pNumber = pNumber

        print("\n>>>  WELCOME ARAB CUISINE (RDX FOODS)  <<<\n\n")
    
    def section(self):
        print("What do you want to have Sir?")
        userInput = input("Food // Refreshments only::")

        if userInput == "Food":
            self.foodMenue()
        else: 
            self.refreshmentsMenue()
        

    def foodMenue(self):
        print("\n^^^Menue^^^")
        print('''\n        Items                       Price
1- Double-Double In-N-Out.          $200
2- Fries Waffells.                  $130
3- Chicken Popeyes.                 $250
4- Chicken Sandwich Chick-fil-A.    $275
5- Curly Fries Arby's.              $90
6- Alfredo Pasta.                   $160''')

        self.placeOrder()

    def refreshmentsMenue(self):
        print("\n^^^Menue^^^")
        print('''\n         Items                       Price
1- Blizzard Dairy Queen.            $65
2- McFlurryy.                       $50
3- Cherry Laimad Sonic.             $80
4- Cappuccino Coffee                $45''')
        
        self.placeOrder()

    def placeOrder(self):
        self.order = input("Place Your Order:: ")
        self.delivery = input("\nDo you want to take HOME or DINNING?\n")
        self.money = self.price(self.order)

    def price(self, order):
        if order.self == "Double":
            print("Your Bill is: $210+tax")
        elif order == "Fries":
            print("Your Bill is: $140+tax")
        elif order == "Chicken Popeyes":
            print("Your Bill is: $260+tax")
        elif order == "Chicken Sandwich":
            print("Your Bill is: $285+tax")
        elif order == "Curly":
            print("Your Bill is: $99+tax")
        elif order == "Al-fredo":
            print("Your Bill is: $170+tax")
        elif order == "Blizzard":
            print("Your Bill is: $75+tax")
        elif order == "Mcflurry":
            print("Your Bill is: $60+tax")
        elif order == "Cherry":
            print("Your Bill is: $90+tax")
        elif order == "Coffee":
            print("Your Bill is: $55+tax")
        else:
            print("Invalid Order...")
        
        self.thankYou()
        
    def thankYou(self):
        print("\nYour Order has been Placed.\n")
        print(f"Thankyou Mr/Mrs: {self.cName}, For Ordering at {self.restaurantName}.")


customer1 = Restaurant("Ali", "Lahore", "0307-5035899")

print(customer1.restaurantName, "\n")

customer1.section()
