import datetime
customers = {}


while True:
    now = datetime.datetime.now()
    print("================================")
    print("   Welcome To MyFresh           ")
    print("================================")
    print("Date & Time:", now.strftime("%d-%m-%Y %H:%M:%S"))
    
    print("\n1. SignUp")
    print("2. Login")
    choice = input("Choose option: ")

    if choice == "1":  
        username = input("Enter the Username: ")
        password = input("Enter your Password: ")
        customers[username] = password
        print("Signup successful! Please Login Now!")

    elif choice == "2":  
        user_name = input("Enter the Username: ")
        pass_word = input("Enter the Password: ")

        if user_name in customers and customers[user_name] == pass_word:
            print("Login Successful!")
            print("Welcome", user_name)

            cart = []

            while True:
                print("\nCategories")
                print("1. Vegetables")
                print("2. Fruits")
                print("3. Dairy")
                print("4. Beverages")
                print("5. Checkout")

                category = input("Choose Your Category: ")

                if category == "1":  
                    print("1. Tomatoes - 50Rs per Kg")
                    print("2. Potatoes - 20Rs per Kg")
                    print("3. Onions - 60Rs per Kg")
                    print("4. LadysFingers - 32Rs per Kg")
                    item = input("Choose items: ")
                    if item == "1":
                        quantity = int(input("Enter quantity in Kg: "))
                        cart.append(("Tomato", 50, quantity))
                        print("Tomatoes added to cart")
                    elif item == "2":
                        quantity = int(input("Enter quantity in Kg: "))
                        cart.append(("Potatos", 20, quantity))
                        print("Potatoes added to cart")
                    elif item == "3":
                        quantity = int(input("Enter quantity in Kg: "))
                        cart.append(("Onions", 60, quantity))
                        print("Onions added cart")
                    elif item == "4":
                        quantity = int(input("Enter quantity in Kg: "))
                        cart.append(("LadysFingers", 32, quantity))
                        print("LadysFingers added cart")
                    else:
                        print("Invalid Item")

                elif category == "2":   
                    print("1. Apples - 5Rs per Apple")
                    print("2. Bananas - 30Rs per Dozen")
                    print("3. Oranges - 3Rs per Orange")
                    print("4. Mangoes - 120Rs per Kg")
                    item = input("Choose items: ")
                    if item == "1":
                        quantity = int(input("Enter how many Apples: "))
                        cart.append(("Apples", 5, quantity))
                        print("Apples added to cart")
                    elif item == "2":
                        quantity = int(input("Enter how many Dozens: "))
                        cart.append(("Bananas", 30, quantity))
                        print("Bananas added to cart")
                    elif item == "3":
                        quantity = int(input("Enter how many Oranges: "))
                        cart.append(("Oranges", 3, quantity))
                        print("Oranges added to cart")
                    elif item == "4":
                        quantity = int(input("Enter quantity in Kg: "))
                        cart.append(("Mangoes", 120, quantity))
                        print("Mangoes added cart")
                    else:
                        print("Invalid Item")

                elif category == "3":   
                    print("1. Milk Packet - 28Rs (500ml)")
                    print("2. Curd Packet - 50Rs (900ml)")
                    print("3. Yogurt Tin - 25Rs (100ml)")
                    print("4. Ghee Tin - 250Rs (500ml)")
                    item = input("Choose items: ")
                    if item == "1":
                        quantity = int(input("How many Milk Packets: "))
                        cart.append(("Milk Packet", 28, quantity))
                        print("Milk Packet added cart")
                    elif item == "2":
                        quantity = int(input("How many Curd Packets: "))
                        cart.append(("Curd Packet", 50, quantity))
                        print("Curd Packet added to cart")
                    elif item == "3":
                        quantity = int(input("How many Yogurt Tins: "))
                        cart.append(("Yogurt Tin", 25, quantity))
                        print("Yogurt Tin added to card")
                    elif item == "4":
                        quantity = int(input("How many Ghee Tins: "))
                        cart.append(("Ghee Tin", 250, quantity))
                        print("Ghee Tin added to cart")
                    else:
                        print("Invalid Item")

                elif category == "4":
                    print("Beverages")
                    print("1. ThumpsUp - 100Rs 2Ltr")
                    print("2. Coke - 76Rs 2Ltr")
                    print("3. RedBull - 105Rs Each 250Ml")
                    print("4. Sprite - 96Rs 2Ltr")
                    item = input("Choose items: ")
                    if item == "1":
                        quantity = int(input("ThumpsUp Bottles Required: "))
                        cart.append(("ThumpsUp", 100, quantity))
                        print("ThumpsUp added to cart")
                    elif item == "2":
                        quantity = int(input("Coke Bottles Required: "))
                        cart.append(("Coke", 76, quantity))
                        print("Coke added to cart")
                    elif item == "3":
                        quantity = int(input("RedBull Tins Required: "))
                        cart.append(("RedBull", 105, quantity))
                        print("RedBull added to cart")
                    elif item == "4":
                        quantity = int(input("Sprite Bottles Required: "))
                        cart.append(("Sprite", 96, quantity))
                        print("Sprite added to cart")
                    else:
                        print("Invalid Input")

                elif category == "5":  
                    if not cart:
                        print("Cart is empty. Please add items first.")
                        continue

                    print("\n==== Bill Summary ====")   
                    total = 0
                    for name, price, quantity in cart:
                        subtotal = price * quantity
                        print(f"{name} x {quantity} = {subtotal} Rs")  
                        total += subtotal   

                    bag = input("Do you want carry bag (Yes/No): ")
                    if bag.lower() == "yes":
                        total += 10
                        print("Carry Bag Charges Added.")
                    print("\n=============================")
                    now = datetime.datetime.now()
                    
                    print( now.strftime("%d-%m-%Y %H:%M:%S"))                          
                    print("\nTotal Bill =", total, "Rs")
                    print("\n=============================")  
                    print("\nChoose Payment Method")
                    print("1. Cash")
                    print("2. Card")
                    print("3. UPI")
                    print("==============================")

                    payment = input("Enter your mode of payment: ")

                    if payment == "1":
                        mode = "Cash"
                    elif payment == "2":
                        mode = "Card"
                    elif payment == "3":
                        mode = "UPI"
                    else:
                        mode = None

                    if mode:
                        print(total, "Rs has been paid through", mode)
                        print("Thank you for shopping with MyFresh,", user_name, "!\n")
                        print(now.strftime("%d-%m-%Y %H:%M:%S"))
                    else:
                        print("Invalid Payment Option")

                    break 
                else:
                    print("Invalid Category Choice")

            print("\n---- Returning to Welcome Screen ----")

        else:
            print("Invalid Username or Password.")

    else:
        print("Invalid Choice Input.")
