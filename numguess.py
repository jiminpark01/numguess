from random import randint
from time import sleep

# Generate answer
answer = randint(1, 100)
print(answer)

# User guess
username = input("What's your name? ")
print(f"Hello, {username}!")
guess = int(input(f"{username}, Guess the number(1-100)!"))
print(f"Your guess is {guess}, right?")


# result
if guess == answer:
    print("**********3**********")
    sleep(1)
    print("**********2**********")
    sleep(1)
    print("**********1**********")
    sleep(1)
    print("That's right!! The answer is {}! Congratulations~!~!".format(answer))

elif guess > answer:
    print(f'Keep going, man~! That was too high, {username}..')

elif guess < answer:
    print(f'Keep going, man~! That was too low, {username}..')

