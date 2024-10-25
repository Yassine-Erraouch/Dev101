#---------------------------------------------functions---------------------------------------------    
#function that asks for a number
def ask_number():
    while True:
        try:
            n=int(input("Enter a number: "))
            return n
        except:
            print("Veuillez entrer un nombre entier")
        

#Q1 :function that checks if number is a palindrome
def estPalindrome(n):
    return str(n) == str(n)[::-1]
    
#Q2 : function that asks for numbers infinite times until user enters a palindrome
def infPalindrom():
    while True:
        if estPalindrome(ask_number()):
            print('le nombre est un palindrome..')
            break
        print("Entrez un nouveau nombre")
#---------------------------------------------menu---------------------------------------------    
while True:
    print("1. pour savoir si un nombre est un palindrome")
    print("2. pour entrez des nombres infiniment jusque qu'un nombre est un palindrome")
    print("3. pour quitter")
    choice = input("Entrez votre choix : ")

    if choice == '1':
        if estPalindrome(ask_number()):
            print("le nombre est un palindrome")
        else:
            print("le nombre n'est pas un palindrome")

    elif choice == '2':
        infPalindrom()

    elif choice == '3':
        break

    else:
        print("Veuillez entrer un choix valide")