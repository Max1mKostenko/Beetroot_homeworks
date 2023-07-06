import random
rand_num = random.randint(1, 10)
user_answer = int(input("Try guess the number in range from 1 to 10: "))
if user_answer == rand_num:
    print("You guessed the number!")
else:
    print("You haven't guessed")
print(f"The computer generated number: {rand_num}")
