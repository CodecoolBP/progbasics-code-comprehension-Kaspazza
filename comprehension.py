import random #using module name you can access the function .random, without writing it on your own

guesses_taken = 0 #assign value 0 to variable

print('Hello! What is your name?') #outputs text
myName = input() #assigning var myName by user input

number = random.randint(1, 20) #assigning var. number, random integer in range 1-20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #outputs text and variable defined earlier

while guesses_taken < 6:  #loop untill var is less than 6
    print('Take a guess.') #outputs text
    guess = input() #assign to var. guess, input made by user
    guess = int(guess) #converts default string input to an integer

    guesses_taken += 1 #adding 1 to a value of var.

    if guess < number: #checking condition if var. guess is lower than var. number
        print('Your guess is too low.') # if it is, that it ouputs text to a user

    if guess > number: #checking condition if var. guess is higher than var. number
        print('Your guess is too high.') #if it is, outputs text

    if guess == number: #checking if the variables are equal
        break           #if they are iteration ends

if guess == number: #checking if variables are equal
    guesses_taken = str(guesses_taken) # converts variable to string
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!') #outputs text and two var.

if guess != number: #checking if variables are not equal
    number = str(number) #if they are, set type of var number to an string
    print('Nope. The number I was thinking of was ' + number) #ouputs text
