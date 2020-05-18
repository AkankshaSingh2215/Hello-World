import random
print("guessing the number")
number = random.randint(1, 9)
chance = 0
print("guess a number")
while chance < 4:
    guess=int(input())

    if guess == number:
       print("congratulations, you won!")
    elif guess < number:
        print("your guess was too low")
    else:
        print("your guess was too high")

chance += 1

if not chances < 4:
    print("you lose!! the number is",number)
         
              
