logo = """
 _____________________
|  _________________  |
| | Pythonista  0.  | |
| |_________________| |
|  ___ ___ ___   ___  |   _____     _      _      _____ 
| | 7 | 8 | 9 | | + | |  / ____|   / \    | |    / ____|
| |___|___|___| |___| | | |       / _ \   | |   | |     
| | 4 | 5 | 6 | | - | | | |      / /_\ \  | |   | |     
| |___|___|___| |___| | | |____ / ___  \ | |___| |____ 
| | 1 | 2 | 3 | | x | |  \_____/_/    \_\|_____|\_____|
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
    
def calculator():
    print(logo)
    calculation={"+":add, 
             "-":subtract,
             "*":multiply,
             "/":divide
              }
    number_1=float(input("What is the first number?: "))
    for symbol in calculation:
        print(symbol)
    operation=input("Pick an operation ")
    number_2=float(input("What is the next number?: "))
    result=calculation[operation](number_1, number_2)
    print(result)
    question=input(f'Type "y" to continue calculating with {result}, or type "n" to start a new calculaton ')
    if question == "y":
        cycle=True
        while cycle:
            for symbol in calculation:
                print(symbol)
            operation=input("Pick an operation ")
            number_2=float(input("What is the next number?: "))
            result=calculation[operation](result, number_2)
            print(result)
            question=input(f'Type "y" to continue calculating with {result}, or type "n" to start a new calculaton: ' )
            if question == "n":
                cycle=False
    elif  question == "n":
        print("\n"*30)
        
        calculator()
calculator()

 