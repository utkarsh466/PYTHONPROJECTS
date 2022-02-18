import random
print("Number guessing game")
print("Guess a number (between 1 and 9) :")
number = random.randint(1, 9)
chance = 5
for i in range(5):
    
    guess = int(input('Enter your guess:-'))
    if(guess == number):
        print("Congratulations YOU WON!!!")
        break
    elif chance == 1:
        print("YOU LOSE!!!, The number is "+ str(number))
        break
    elif guess < number:
        print("Your guess was too low: Guess a number higher than " + str(guess))      
        chance = chance-1
    elif guess > number:
        print("Your guess was too higher: Guess a number lower than " + str(guess))
        chance = chance-1    

    