# Sam has been dumped by his girlfriend so he's gone into the local milk 
# bar to drown his sorrows. He has a budget, and there's a choice of three (or more) 
# milkshakes, differently priced. The barman says, "What can I fix you?" and Sam can reply with a 
# number corresponding to the relevant flavour - this list is displayed every iteration. 
# If he enters Q, he quits and leaves; the barman wishes him well in his search for love. 
# If he orders but can't pay he's thrown out.

def main():
    milkshakes = { "Vanilla": 3.50, "Chocolate": 4.00, "Strawberry": 3.75 }
    budget = float(input("What is your budget? £"))
    print("What can I fix you", milkshakes)

    while True: 
        print("\nAvailable Milkshakes:") 
        for flavor, price in milkshakes.items(): 
            print(f"{flavor} - ${price:.2f}") 
        print("Q. Quit")
    
        choice = input("Select a milkshake by flavor or 'Q' to quit: ").capitalize()

        if choice == 'Q':
            print("Goodbye!")
            break

        if choice in milkshakes:
            price = milkshakes[choice]
            if price > budget:
                print("You can't afford that.")
            else:
                budget -= price
                print(f"You ordered {choice}. Remaining budget: ${budget:.2f}")
        else:
            print("Invalid choice.")

main()
