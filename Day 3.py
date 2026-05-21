# print("Welcome to the roller coaster!")
# height=int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# number=int(input("What is the number you want to check? "))
# if number%2== 0:
#     print("Even")
# else:
#     print("Odd")

# print("Welcome to the roller coaster!")
# height=int(input("What is your height in cm? "))
# bill=0
# if height >= 120:
#     print("You can ride rollercoaster")
#     age=int(input("What is you age? "))
#     if age <= 12:
#         bill=5
#         print("Children tickets are $5")
#     elif age <= 18:
#         bill=7
#         print("Youth tickets are $7")
#     elif 45 <= age >= 55:
#         print("Everything is going to be ok. Have a free ride on us")
#     else:
#         bill=12
#         print("Adults tickets are $12")
#     wants_photo=input("Do you want to have a photo take, type (y) for Yes or (n) for No. ")
#     if wants_photo == "y":
#         bill+=3
#     print(f"Your final bill is ${bill}")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# print("Welcome to Python Pizza deliveries!")
# size=input("What size Pizza do you want? (S) fo small, (M) for medium and (L) for large. ").lower()
# pepperoni=input("Do you want pepperoni? (y) for Yes or (n) for No. ").lower()
# extra_cheese=input("Do you want to extra cheese? (y) for Yes or (n) for No. ").lower()
# bill=0
# if size == "s":
#     bill+=15
# elif size == "m":
#     bill+=20
# elif size == "l":
#     bill+=25
# else:
#     print("You typed the wrong input.")
# if pepperoni == "y":
#     if size == "s":
#         bill+=2
#     else:
#         bill+=3
# if extra_cheese == "y":
#     bill+=1
# print(f"Your total bill is ${bill}.")


print("Welcome to Treasure Island! \nYour mission is to find the treasure.")
sides = input("You are at a cross road . Where you want to go? \nType (left) or (right)? ").lower()
if sides == "left":
    option_1=input("You have came to lake? Type (swim) or (wait) ").lower()
    if option_1 == "wait":
        print("You arrived at the island unharmed. There is a house with 3 doors ")
        doors = input("One red, One yellow and one blue. Which color do you choose? ").lower()
        if doors == "yellow":
            print("You win.")
        else:
            print("Game over.")
    else:
        print("Game over.") 
else:
    print("Game over!")









