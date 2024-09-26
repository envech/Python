import random
print ('This is a game. You need to guess the number')
secret_number = random.randint (1, 10)
attempts = 0
while True:
    guess = int(input('Enter the number:'))
    attempts += 1
    if guess == secret_number:
        print (f'Right! You guessed the number in {attempts} tries')
        break
    elif guess < secret_number:
        print ('Your guess is less than the number')
    else:
        print ('Your guess is greater than the number')