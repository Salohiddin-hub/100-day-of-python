# def greet(name, location):
#     print(f"Assalomu alaykum, {name}")
#     print("How is it going?")
#     print("How is your studies?")
#     print(f"I am now in {location}")
# greet("Abdulloh", "Korea")

# def life_in_weeks(years):
#     weeks=(90-years)*52
#     print(f"You have {weeks} left")
# life_in_weeks(56)

# def calculate_love_score(name1="Angela Yu", name2="Jack Bauer"):
#     both_nam=(name1+name2).lower()
#     both_name=both_nam.lower()
#     t=both_name.count("t")
#     r=both_name.count("r")
#     u=both_name.count("u")
#     e=both_name.count("e")
#     number=t+r+u+e
#     l=both_name.count("l")
#     o=both_name.count("o")
#     v=both_name.count("v")
#     e=both_name.count("e")
#     love=l+o+v+e
#     result=str(number)+str(love)
#     return result
    
# print(calculate_love_score("Kanye West", "Kim Kardashian"))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# text=input("Type your message: \n").lower()
# shift=int(input("Type the shift number \n"))
# def encrypt(a=text, b=shift):
#     whole=""
#     for letter in text:
#         original_text=alphabet.index(letter)
#         original_text+=shift
#         original_text %= len(alphabet)
#         shift_amount=alphabet[original_text]
#         whole+=shift_amount
#     return f"Here is the encoded result: {whole}"
# print(encrypt())
# def decrypt(a=text, b=shift):
#     decrypted_version=""
#     for letter in text:
#         w_index=alphabet.index(letter)
#         w_index-=shift
#         w_index %= len(alphabet)
#         decrypted=alphabet[w_index]
#         decrypted_version+=decrypted
# #     return f" This is the decoded result: {decrypted_version}"
# text=input("Type your message: \n").lower()
# shift=int(input("Type the shift number \n"))
# direction=input("Type 'encode' to encrypt(), Type 'decode' to decrypt: \n").lower()
# def encrypt(a=text, b=shift):
#     text=input("Type your message: \n").lower()
#     whole=""
#     for letter in text:
#         text=alphabet.index(letter)
#         text+=shift
#         text %= len(alphabet)
#         shift_amount=alphabet[text]
#         whole+=shift_amount
#     return f"Here is the encoded result: {whole}"
# print(encrypt())
# def decrypt(a=text, b=shift):
#     shift=int(input("Type the shift number \n"))
#     decrypted_version=""
#     for letter in text:    
#         text=alphabet.index(letter)
#         text+=shift
#         text %= len(alphabet)
#         shift_amount=alphabet[text]
#         decrypted_version+=shift_amount
#     return f" This is the decoded result: {decrypted_version}"

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP_______  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP_______ 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""



# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# def caeser(text, shift, encode_or_decode ):
#         output=""
#         if encode_or_decode == "decode":
#             shift*=-1
#         for letter in text:
#             if letter not in alphabet:
#                 output+=letter
#             else:
#                 original_index=alphabet.index(letter)
#                 new_index = (original_index + shift) % len(alphabet)
#                 output+=alphabet[new_index]
#         print(f"Here is the {encode_or_decode}d result: {output}")
# print(logo)
# cycle=True
# while cycle:
#     direction=input("Type 'encode' to encrypt(), Type 'decode' to decrypt: \n").lower()
#     text=input("Type your message: \n").lower()
#     shift=int(input("Type the shift number \n"))
#     caeser(text, shift, direction )
#     restart=input("Type 'yes' if you want to go again. Otherwise type 'no': \n").lower()
#     if restart == "no":
#          cycle=False
#          print("Goodbye")


# List of all letters in the alphabet used for indexing
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text, shift, encode_or_decode):
    output = ""
    # If the user wants to decode, multiply the shift by -1 to move backwards
    if encode_or_decode == "decode":
        shift *= -1
    
    for letter in text:
        # If the character is a symbol/number, add it to the output as-is
        if letter not in alphabet:
            output += letter
        else:
            # Find the position of the current letter in the alphabet list
            original_index = alphabet.index(letter)
            # Add the shift to the index and use modulo to wrap around from z to a
            new_index = (original_index + shift) % len(alphabet)
            # Build the output string with the new shifted letter
            output += alphabet[new_index]
            
    print(f"Here is the {encode_or_decode}d result: {output}")

# Print the ASCII art logo from the start
print(logo)

cycle = True
# Loop keeps the program running until the user types 'no'
while cycle:
    # Gather user inputs for the direction, the message, and the shift amount
    direction = input("Type 'encode' to encrypt(), Type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number \n"))
    
    # Call the function with the gathered data
    caeser(text, shift, direction)
    
    # Check if the user wants to restart or exit
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no': \n").lower()
    if restart == "no":
        cycle = False
        print("Goodbye")