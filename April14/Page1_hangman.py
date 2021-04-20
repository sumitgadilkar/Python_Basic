word = 'apple'
lives = 3

# _____
answer = '_' * len(word)

print(f"Welcome to Hangman.\nYou need to guess a word by guessing all the letters in the word.\nYou will have {lives} lives.\nIf you guess the entire word before loosing the lives, you will win the game.")
print()
print("Your word is")
print(answer)
print()
print('-' * 80)


while lives > 0:
    # get a letter from user
    letter = input(f"You have got {lives} lives. Guess a letter: ")
    print(f"you have guessed: {letter}")

    if (letter in word) and (letter not in answer):
        print(f"Your guess right")

        # list is mutable
        characters = list(answer)
        index = 0
        for char in word:
            # check if user's letter is present in the word
            if char == letter:
                # replace the position with the right letter
                characters[index] = letter
            index += 1

        # construct answer string again with a letter replacement
        answer = ''.join(characters)
        print(answer)

        # check if user has guessed all the letters
        if '_' not in answer:
            print(f"Congratulations!!! You have guessed all the letters. You won the Game.")
            break

    else:
        print(f"Your guess is wrong. You have lost one life.")
        lives -= 1

        if lives == 0:
            print(f":( You have lost the Game!!!")

    print('-' * 80)