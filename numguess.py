from random import randint
from time import sleep

def play(N, guess, answer):
    for i in range(N):
        if guess == answer:
            return 1
        elif guess > answer:
            print(f'That was too high, {username}.. Try again!')
            guess = int(input("Guess the number(1-100)! "))
        else:
            print(f'That was too low, {username}.. Try again!')
            guess = int(input("Guess the number(1-100)! "))


# Generate answer
answer = randint(1, 100)
print(answer)

# User guess
username = input("What's your name? ")
print(f"Hello, {username}!")
guess = int(input(f"{username}, You have 7 chances. Guess the number(1-100)! "))
print(f"Your guess is {guess}, right?")


# result
win = play(6, guess, answer)

if win == 1:
    print("Hmm...")
    sleep(1)
    print("That's right!! The answer is {}! Congratulations~!~!".format(answer))
else:
    print("----GAME OVER----")

