print("Hello, my name is John and I will be your assistant for today. I am here to help you order pizza!")
print("\n To get started, I need to ask you a few questions. After typing your answer, press enter.")
userName = input("\nEnter your name:  ")
while len(userName) == 0:
    userName = input("Name cannot be blank! Please enter your name: ")
    
if userName.lower() == "robert dennis":
    print(f"\nMy creator, {userName}. Pleasure to serve you!")
else:
    print(f"Hello, {userName}. Nice to meet you!")
keepGoing = "y"
while keepGoing.lower() == "y":
    size = input("\n What size do you want? Enter small, medium or large:  ")
    while size.lower() not in ["small","medium","large"]:
        size = input("Invalid value! Please enter small, medium or large:  ")
    
    flavor = input("\n Enter the flavor of pizza:  ")
    while len(flavor) == 0:
        flavor = input("The flavor cannot be blank! Please enter your requested flavor of pizza: ")
    
    crustType = input("\n What type of crust do you want:  ")
    while len(crustType) == 0:
        crustType = input("The type of crust cannot be blank! Please enter the type of crust you want: ")
    
    quantity = input("\n How many of these do you want to order? Enter a numeric value:  ")
    while not quantity. isdigit():
        quantity = input("Value not recognized. Please enter a numeric value:  ") 
    
    quantity = int(quantity)
    method = input("\n Is this carry out or delivery:  ")
    while method not in ["carry out","delivery"]:
        method = input("Invalid value! Please enter carry out or delivery:  ")

    while size.lower() not in ["small","medium","large"]:
        size = input("Invalid value! Please enter small, medium or large:  ")
    if method.lower() == "delivery":
        deliveryFee = 5
    else: 
        deliveryFee = 0
    if size.lower() == "small":
        pizzaCost = 8.99
    elif size.lower() == "medium":
        pizzaCost = 14.99
    elif size.lower() == "large":
        pizzaCost = 17.99
    salesTax = 1.1
    total = (pizzaCost * quantity) * salesTax + deliveryFee
    print("-" * 10)
    print(f"Thank you, {userName}, for your order. ")
    print(f" Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")
    if total >= 50:
        print("\nCongratulations! You've been awarded a $10 off coupon for your next order.")
    else:
        print("\nOrder over $50 will receive a free $10 off coupon!")
    print("-" * 10)
    print("Order has been received. ETA 3 mins!")
    for min in range(3, 0, -1):
        print(min, "minutes remaining")
        for seconds in range(60, 0, -1):
            print(seconds, end = "\r")
            import time
            time.sleep(1)
    print("order is ready! ")
    keepGoing = input("Do you want to place another order? Enter y or n:  ")
    while keepGoing.lower() not in ["y", "n"]:
        keepGoing = input("Invalid Value: Enter y or n:  ")