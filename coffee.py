# Initial variables
water = 400
milk = 540
beans = 120
cups = 9
money = 550
# Last order water, milk, beans, cup, money
last_order = [0,0,0,0,0]
# Print state
def state():
    print("The coffee machine has:")
    print("{0} of water".format(water))
    print("{0} of milk".format(milk))
    print("{0} of coffee beans".format(beans))
    print("{0} of disposable cups".format(cups))
    print("{0} of money".format(money))

# make coffe
def change_state(water_ = 0, milk_ = 0, beans_ = 0, cups_ = 1, money_ = 0):
    # accessing global variables
    global water, milk, beans, cups, money 
    
    water -= water_
    milk -= milk_
    beans -= beans_
    cups -= cups_
    money += money_

run = True

while(run == True):
    print("Write action (buy, fill, take, remaining, exit):")
    choice = input()

    if choice == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        user_input = input()
        
        # espresso 250 ml water and 16g coffee beans. costs $4
        if user_input == "1":
            if  water >= 250 and beans >= 16 and cups >= 1:
                last_order = [250, 0, 16, 1, 4]
                change_state(250, 0, 16, 1, 4)
                print("I have enough resources, making you a coffee!")
            else:
                if water < 250:
                    print("Sorry, not enough water!")
                elif cups < 1:
                    print("Sorry, not enough disposable cups!")
                else:
                    print("Sorry, not enough coffee beans!")
        # latte, 350 ml of water, 75 ml of milk, and 20 g of coffee beans. costs $7.
        elif user_input == "2":
            if water >= 350 and milk >= 75 and beans >= 20 and cups >= 1:
                last_order = [350, 75, 20, 1, 7]
                change_state(350, 75, 20, 1, 7)
            else:
                if water < 350:
                    print("Sorry, not enough water!")
                elif milk < 75:
                    print("Sorry, not enough milk!")
                elif cups < 1:
                    print("Sorry, not enough disposable cups!")
                else:
                    print("Sorry, not enough coffee beans!")
        # cappuccino, 200 ml of water, 100 ml of milk, and 12 g of coffee. costs $6.
        elif user_input == "3":
            if water >= 200 and milk >= 100 and beans >= 12 and cups >= 1:
                last_order = [200, 100, 12, 1, 6]
                change_state(200, 100, 12, 1, 6)
            else:
                if water < 200:
                    print("Sorry, not enough water!")
                elif milk < 100:
                    print("Sorry, not enough milk!")
                elif cups < 1:
                    print("Sorry, not enough disposable cups!")
                else:
                    print("Sorry, not enough coffee beans!")
        # user enters "back" 
        else:
            change_state(*last_order)
    if choice == "fill":
        # get input
        print("Write how many ml of water do you want to add:")
        water += int(input())
        print("Write how many ml of milk do you want to add:")
        milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        cups += int(input())
    if choice == "take":
        print("I gave you ${0}".format(money))
        money = 0
    if choice == "remaining":
        state()
    if choice == "exit":
        run = False