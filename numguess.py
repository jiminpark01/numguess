from random import randint

# Generate answer
answer = randint(1, 100)
print(answer)

# User guess
username = input("What's your name? ")
print(f"Hello, {username}!")

guess = input(f"{username}, Guess the number(1-100)!")
print(f"Your guess is {guess}, right?")


