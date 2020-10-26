# Created by Shayokh Shorfuddin [Busy Studying😅😅]

alphabet_capital = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

alphabet_small = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

numbers = [1,2,3,4,5,6,7,8,9,10]

symbols = ['+','=','%','_','|','<','>','!','@','#','$','/','^','&','*','\',']


import random

randomalphabet_capital = random.choice(alphabet_capital)

randomalphabet_capital2 = random.choice(alphabet_capital)

finalrandomalphabet_capital = randomalphabet_capital + randomalphabet_capital2 

randomalphabet_small = random.choice(alphabet_small)

randomalphabet_small2 = random.choice(alphabet_small)


finalrandomalphabet_small = randomalphabet_small + randomalphabet_small2 

randomnumber = str(random.choice(numbers))

randomnumber2 = str(random.choice(numbers))

finalrandomnumber = randomnumber + randomnumber2

randomsymbol = random.choice(symbols)

randomsymbol2 = random.choice(symbols)

finalrandomsymbol = randomsymbol + randomsymbol2

full = (finalrandomalphabet_capital + finalrandomnumber + finalrandomsymbol + finalrandomalphabet_small+ finalrandomsymbol + finalrandomalphabet_capital)

def add():
 print(input("Enter victim's Instagram username:"))
 print("Looking for injection point...")
 print("Point found!")
 print("Injecting...")
 print("Hacked!")
 print("Password = " + full)
add()





