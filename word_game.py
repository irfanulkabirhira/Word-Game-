import random

stages = ['''
 +----+
 |    |
 0    |
/|\   |
/ \   |
      |
==========
''','''
 +----+
 |    |
 0    |
/|\   |
/     |
      |
==========

''' , '''
 +----+
 |    |
 0    |
/|\   |
      |   
==========
''' , '''

 +----+
 |    |
 0    |
/|    |     
      |
      |
==========

''' , '''
 +----+
 |    |
 0    |
 |    |
      |
      |     
==========

''' , '''
 +----+
 |    |
 0    |
      |
      |
==========
''' , '''
 +----+
 |    |
      |
      |
      |
==========

''']


word_list = ["aardvark" , "baboon" , "camel"]

# Create a variable called 'Lives' to keep the track of lives left
# Set 'Lives' to equal 6.
lives = 6


chosen_word = random.choice(word_list)
print(chosen_word)


# step 1 : To Create a placeholer
placeholder = ""
word_lentgh = len(chosen_word)
for position in range(word_lentgh):
    placeholder+="_"
print(placeholder)

# Use a while loop to let user guess again
game_over = False
correct_letters = []
while not game_over:
    # TODO-6 : Update the code below to tell the user how many lives they have left .
    print(f"*********<???> {lives}/6 LIVES Left ***************")
    guess = input("Guess a letter lower: ").lower()

    # TODO-4: Id the user entered a letter thet have already guess, print the letter
    display = " "

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # Step 2: If guess is not letter in the Chosen_word, then reduce 'Lives' by 1
    # If lives guess down to 0 then the game should stop and it should prind "You lose the game"

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"*************** It was {chosen_word}! You loss The game,Wish You all the Best for the next time !!******************")

    if "_" not in display:
        game_over=True
        print("***********You Win.!!****************")

    # Step 3 : Print the Asci Art from the satges
    # that Corresponsing to the current number of 'lives' the uses has remaining.

    print(stages[lives])



