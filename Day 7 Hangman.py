import random
food_list=["apple", 'banana', "apricot", "peach"]
r_word=random.choice(food_list).lower()
word_length=len(r_word)
STAGES = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    """, # 6 failures: Game Over
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |
    """, # 5 failures
    """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |
    """, # 4 failures
    """
       ------
       |    |
       |    O
       |   /|
       |    
       |
    """, # 3 failures
    """
       ------
       |    |
       |    O
       |    |
       |    
       |
    """, # 2 failures
    """
       ------
       |    |
       |    O
       |    
       |    
       |
    """, # 1 failure
    """
       ------
       |    |
       |    
       |    
       |    
       |
    """  # 0 failures: Start
]
game_over=False
corrected_list=[]
lives=6
while not game_over:
    
    display=""
    user=input("Enter your letter: ").lower()
    print(user)
    if user in corrected_list:
        print (f"You have already entered this letter!")
    if user not in r_word:
        lives-=1
        print(f"You guessed {user}: that's not in the word. You lose a life ")
        if lives == 0:
            game_over=True
            print(f"{r_word}. You lose")  
    for letter in r_word:
         
         if letter == user:
            display+=letter
            corrected_list.append(letter)
         elif letter in corrected_list:
             display+=letter 
         elif letter != user:
            display+="_"
    print(display)
        
    if "_" not in display:
        game_over=True
        print("You won")
    print(STAGES[lives])
    