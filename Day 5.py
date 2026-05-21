# student_scores=[15, 90, 100, 199, 68]
# max_score=0
# for score in student_scores:
#     if score > max_score:
#         max_score=score
# print(max_score)

# total=0
# for number in range(1,101):
#     total+=number
# print(total)

# for number in range(1,101):
#     if number %3 == 0 and number %5 ==0:
#         print("FizzBuzz")
#     elif number %3 == 0:
#         print("Fizz")
#     elif number %5 == 0:
#         print("Buzz")
#     else:
#         print(number)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_list=[]
for letter in (0,nr_letters):
    password_list.append(random.choice(letters))
for symbol in (0, nr_symbols):
    password_list.append(random.choice(symbols))
for number in (0, nr_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
password=""
for i in password_list:
    password+=i
print(password)    