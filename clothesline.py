import random
print("Wlcome to Clothesline! ")
# easy_words = []
# easy_words_file = open("easy_words.txt", "r")
# easy_words_read = easy_words_file.readlines()
# easy_words.append(easy_words_read)


def main():
    clear_screen()

    #secret_word = pick_secret_word()
    secret_word = pick_word()

    message = "The secret word is: " 

#print(message + " " + secret_word)

    secret_word_length = len(secret_word)
#print(message + " " + secret_word + " " +str(secret_word_length))

    guess = "-" * secret_word_length

    # print("Guess a letter...if you dare!")
    # letter = input("> ")
    # print(letter)



    # is_correct = is_letter_in_word(letter, secret_word)

    # if is_correct == True:
    #     print("Good Guess! ")
    # else:
    #     print("You're terrible at guessing. ")

    incorrect_count = 0
    letters_guessed = []

    while incorrect_count < 8 and guess != secret_word:
        clear_screen()
        print()
        print()


        print_clothesline(incorrect_count)
        print()
        print()
        print("Word:    " + guess)
        print()
        print("Guesses:  " + " ".join(letters_guessed)) #prints list of guesses with a single space between
        print()

        print("Guess a letter...if you dare!")
        print()
        letter = input("> ") #only takes the first letter of user input (dog = d)
        while letter == "":
            letter = input("> ")
        letter = letter[0]
        print()
        print(letter)
        # letters_guessed = []
        letters_guessed.append(letter)
        #print("Guesses:  " + str(letters_guessed))


        is_correct = is_letter_in_word(letter, secret_word)

        if is_correct == True:
            #print("Good Guess! ")
            guess = update_guess(guess, letter, secret_word)
        else:
            #print("You're terrible at guessing. ")
            incorrect_count = incorrect_count + 1

    clear_screen()
    print()
    print()


    print_clothesline(incorrect_count)
    print()
    print()
    print("Word:    " + guess)
    print()
    print("Guesses:  " + " ".join(letters_guessed))
    print()

    if guess == secret_word:
        print("You Win! The Word Was " + secret_word)
    else:
        print("You Did Not Win. The Word Was " + secret_word)
       


def update_guess(old_guess, letter,  word):
    new_guess = ""
    for index in range(len(old_guess)):
        if word[index] == letter:
            new_guess = new_guess + letter
        else:
            new_guess = new_guess + old_guess[index]

    return new_guess


def print_clothesline(incorrect_count):
    chances = 8 - incorrect_count
    print("Incorrecet guesses left " + str(chances))
    # Clothesline ASCII Art
    if incorrect_count == 0:
        print(clothesline_0)
    elif incorrect_count == 1:
        print(clothesline_1)
    elif incorrect_count == 2:
        print(clothesline_2)
    elif incorrect_count == 3:
        print(clothesline_3)
    elif incorrect_count == 4:
        print(clothesline_4)
    elif incorrect_count == 5:
        print(clothesline_5)
    elif incorrect_count == 6:
        print(clothesline_6)
    elif incorrect_count == 7:
        print(clothesline_7)
    elif incorrect_count == 8:
        print(clothesline_8)

clothesline_0 = r"""
=====!=====!=======!=====!=======!=====!=======!=====!=====
    /'''V'''\     /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |       |     |
     |     |       |     |       |     |       |     |
     ```````       ```````       ```````       ```````


"""

clothesline_1 = r"""
=====!=====!=======!=====!=======!=====!=======!===========
    /'''V'''\     /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |       |     |      |   |
     |     |       |     |       |     |      |   |
     ```````       ```````       ```````      `-._|


"""

clothesline_2 = r"""
=====!=====!=======!=====!=======!=====!===================
    /'''V'''\     /'''V'''\     /'''V'''\
/         \   /         \   /         \
'-"|     |"-' '-"|     |"-' '-"|     |"-'
    |     |       |     |       |     |
    |     |       |     |       |     |
    ```````       ```````       ```````
                                            _.~.,_.._
                                            ```````

"""

clothesline_3 = r"""
=====!=====!=======!=====!=======!=========================
    /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |      |   |
     |     |       |     |      |   |
     ```````       ```````      `-._|
                                            _.~.,_.._
                                            ```````
"""

clothesline_4 = r"""
=====!=====!=======!=====!=================================
    /'''V'''\     /'''V'''\
   /         \   /         \
  '-"|     |"-' '-"|     |"-'
     |     |       |     |
     |     |       |     |
     ```````       ```````
                            _.~.,_.._     _.~.,_.._
                            ```````       ```````
"""

clothesline_5 = r"""
=====!=====!=======!=======================================
    /'''V'''\     /'\
   /         \   /   .\
  '-"|     |"-'  '|  ='
     |     |      |   |
     |     |      |   |
     ```````      `-._|
                            _.~.,_.._     _.~.,_.._
                            ```````       ```````
"""

clothesline_6 = r"""
=====!=====!===============================================
    /'''V'''\
   /         \
  '-"|     |"-'
     |     |
     |     |
     ```````
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                ```````       ```````       ```````
"""

clothesline_7 = r"""
=====!=====================================================
    /'\
   /   .\
   '|  ='
    |   |
    |   |
    `-._|
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                ```````       ```````       ```````
"""

clothesline_8 = r"""
===========================================================






_.~.,_.._     _.~.,_.._     _.~.,_.._     _.~.,_.._
```````       ```````       ```````       ```````
"""


def pick_secret_word():
    secret_word_options = ["apple", "pear", "banana", "scorpion", "umbrella"]
    random_secret_word = random.choice(secret_word_options)
    return random_secret_word

def pick_word():
    word_filename = "easy_words.txt"
    word_file = open(word_filename)
    all_text = word_file.read()
    all_words = all_text.splitlines()
    word_file.close()

    word = random.choice(all_words)
    return word

def is_letter_in_word(letter, word):
    if letter in word:
        return True
    else:
        return False


def clear_screen():
    print("\033[H\033[J", end="")

main()