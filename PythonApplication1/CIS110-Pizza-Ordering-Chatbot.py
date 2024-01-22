print("Hello, my name is John and I will be your assistant for today. I am here to help you order pizza!")
print("\n To get started, I need to ask you a few questions. After typing your answer, press enter.")
userName = input("\nEnter your name:  ")
print(f"Hello, {userName}. Nice to meet you!")
size = input("\n What size do you want? Enter small, medium or large:  ")
flavor = input("\n Enter the flavor of pizza:  ")
crustType = input("\n What type of crust do you want:  ")
quantity = input("\n How many of these do you want to order? Enter a numeric value:  ")
quantity = int(quantity)
method = input("\n Is this carry out or delivery:  ")
pizzaCost = 14.99
salesTax = 1.1
total = (pizzaCost * quantity) * salesTax
print("-" * 10)
print(f"Thank you, {userName}, for your order. ")
print(f" Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")
print("-" * 10)
