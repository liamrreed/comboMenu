# Liam Reed
# Project 3.1.3
# Combo Menu Program
# Began 2/28/23
total_cost = 0
sandwich_choice = ""
drink_size = ""
fries_size = ""
ketchup_packets = 0
mega_size = False
order = []
running = True
all_customers = []
# Prompt user on the type of sandwich they'd prefer
while running:
    sandwich_choice = input("What type of sandwich would you like?\nChicken ($5.25), Beef ($6.25), or Tofu? ($5.75)\n> ").lower().strip()
    if sandwich_choice == "chicken":
        total_cost += 5.25
        order.append("chicken")
    if sandwich_choice == "beef":
        total_cost += 6.25
        order.append("beef")
    if sandwich_choice == "tofu":
        total_cost += 5.75
        order.append("tofu")
    print("You selected the " + sandwich_choice + " meat choice.\n")
    # Prompt user on whether or not they would like a beverage
    beverage = input("Would you like a beverage?\n> ").lower().strip()
    if beverage == "yes":
        drink_size = input("What size would you like? Small ($1.00), Medium ($1.75), or Large ($2.25)?\n> ").lower().strip()
        print("You selected the " + drink_size + " drink size.\n")
    if drink_size == "small":
        total_cost += 1.0
        order.append("small")
    if drink_size == "medium":
        total_cost += 1.75
        order.append("medium")
    if drink_size == "large":
        total_cost += 2.25
        order.append("large")
    # Prompt user on if they would like french fries
    fries = input("Would you like french fries?\n> ").lower().strip()
    if fries == "yes":
        fries_size = input("What size french fries would you like? Small ($1.00), Medium ($1.50), or Large ($2.00)?\n> ").lower().strip()
        print("You selected the " + fries_size + " fries size.\n")
    if fries_size == "small":
        total_cost += 1.0
        order.append("small")
    elif fries_size == "medium":
        total_cost += 1.5
        order.append("medium")
    elif fries_size == "large":
        total_cost += 2.0
        order.append("large")
    
    # Prompt user on if they would like to size up their fries
    if fries_size == "small":
        mega_size = input("Would you like to mega-size your fries?\n> ").lower().strip()
        if mega_size == "yes":
            fries_size == "large"
            total_cost += 1.0
            order.remove("small")
            order.append("large")
    
    # Prompt the user on how many ketchup packets they would like
    packets = int(input("\nHow many ketchup packets would you like?\n> "))
    if packets > 0:
        total_cost += 0.25 * packets
        order.append(packets)
    if fries == "yes" and beverage == "yes":
        total_cost -= 1.0
    all_customers.append(order)
    order = []
    running = bool(int(input("Would you like to place another order? Enter a 0 to end your order and enter a 1 to continue ordering.\n> ")))
for customer in all_customers:
    print(f"You ordered a {customer[0]} sandwich, a {customer[1]} drink" + 
         f" and {customer[2]} fries, with {customer[3]} ketchup packets.")
print("Your total comes out to " + "$" + str(total_cost) + " dollars. Thanks!")
