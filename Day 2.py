# print(type(12.1))
# print(type(12))
# print(type(False))
# print(type("Assalom"))
# print("The number of letters in your name: " + str(len(input("Enter your name \n"))))

print("Welcome to the tip calculator")
total_bill=float(input("What was the total bill?\n>>>$"))
tip=int(input("How much tip would you like to give 10, 12 or 15?\n>>>"))
split=int(input("How many people to split the bill? \n>>>"))
tip=1+(tip/100)
bill=(total_bill/split)*tip
print(f"Each person should pay: ${bill}")
