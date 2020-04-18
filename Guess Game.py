import random
def level(num, guesses, random_num):
    count = 0
    while count < guesses:
        y = True
        while y == True:
            try:
                guess_number = int(input('GUESS: '))
                y = False
            except ValueError:
                print('Enter an integer')
        count = count + 1
        if guess_number in range(num + 1):
            if guess_number == guess_number:
                if guess_number == random_num:
                    print('YOU GOT IT RIGHT')
                    break
                elif guess_number != random_num:
                    print('That is wrong')
                    print(f'you have {guesses-(count)} guess left')
        else:
            count = count - 1
            print(f'Enter a number between 1 and {num}')
            print(f'you have {guesses-(count)} guess left')
    else:
        print(f'THE NUMBER IS {random_num}')
        print('GAME OVER')


print("Select the level of difficulty ")
print("ENTER EASY: The Number is between 1-10 and You have 6 guesses")
print("ENTER MEDIUM: The Number is between and You have 4 guesses")
print("ENTER HARD: 1-50 and 3 guesses")
x=True
while x==True:
    difficulty=input("Enter a level: ").lower()
    if difficulty=="easy":
        max_num=10
        rand_num=random.randint(1,max_num)
        guess=6
        level(max_num,guess,rand_num)
        x=False
    elif difficulty=="medium":
        max_num=20
        rand_num=random.randint(1,max_num)
        guess=4
        level(max_num,guess,rand_num)
        x=False
    elif difficulty=="hard":
        max_num=50
        rand_num=random.randint(1,max_num)
        guess=3
        level(max_num,guess,rand_num)
        x=False
    else:
        print("Your entry is wrong, TRY AGAIN")