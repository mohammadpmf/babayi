from random import randint
answer = randint(1, 100)
# print(answer)
while True:
    guess = int(input("Guess: "))
    if guess == answer:
        print("Right answer")
        break
    elif guess>answer:
        if guess>answer+10:
            print("Guess is too big")
        else:
            print("Guess is big")
    else:
        if guess<answer-10:
            print("Guess is too small")
        else:
            print("Guess is small")


