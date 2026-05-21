# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
# student_grades={}
# for student in student_scores:
#     score=student_scores[student]
#     if score <= 91:
#         student_grades[student]="outstanding"
#     elif score <= 81:
#         student_grades[student]="Exceeds expectations"
#     elif score <=71:
#         student_grades[student]="Acceptable"
#     elif score <= 70:
#         student_grades[student]="Fail"
# print(student_grades)
logo = '''
                         ___________
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
""" Secret Auction Program.
A command-line blind auction application that collects names and bids 
in a dictionary, clears the screen between users, and determines the 
highest bidder once all participants have finished.
"""
print(logo)
print("Welcome to the secret auction program.")
cycle=True
bids={}
while cycle:
    user_k=input("What is your name? \n")
    user_v=int(input("What`s your bid? \n"))
    user_c=input("Are there any other bidders? Type 'yes' or 'no'. \n")
    bids[user_k]=user_v
    if user_c == "yes":
        print("\n" * 100)
    elif user_c == "no":
        cycle=False
        h_price=0
        winner=""
        for name in bids:
            bid_amount=bids[name]
            if bid_amount > h_price:
                h_price=bid_amount
                winner=name.capitalize()
        print("\n" * 100)        
        print(f"Winner is {winner} with a bid of ${h_price}")


def highest_price(bidding_dictionary):
    h_price=0
    winner=""
    for name in bids:
        bid_amount=bids[name]
        if bid_amount > h_price:
            h_price=bid_amount
            winner=name
    print(f"Winner is {winner} with a bid of ${h_price}") 

print(logo)
print("Welcome to the secret auction program.")
cycle=True
bids={}
while cycle:
    user_k=input("What is your name? \n")
    user_v=int(input("What`s your bid? \n"))
    user_c=input("Are there any other bidders? Type 'yes' or 'no'. \n")
    bids[user_k]=user_v
    if user_c == "yes":
        print("\n" * 100)
    elif user_c == "no":
        cycle=False
        highest_price(bids)
              
