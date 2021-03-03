from random import randrange
break_flag = 0
guesses_list = []
random_num = randrange(1, 30)
guess_num = input("Introduce your guess (1-30): ")
while True:
    if(guess_num == "Exit" or guess_num == "exit" or guess_num == "EXIT"):
        print("FINISH PROGRAM")
        break_flag = 1
    else:
        guess_num = int(guess_num)
        if(guess_num == random_num):
            print("You got it!")
            guesses_list.append(guess_num)
            break_flag = 1
        elif(guess_num < random_num):
            guesses_list.append(guess_num)
            guess_num = input("Your guess is too low. Try again: ")
        elif(guess_num > random_num):
            guesses_list.append(guess_num)
            guess_num = input("Your guess is too high. Try again: ")
        else: print("FINISH PROGRAM")
    if(break_flag): break
print("\nYour guesses:\n")
with open('GuessingSteps.txt', 'w') as f:
    for guess in guesses_list:
        print(guess)
        f.write("%s\n" % guess)