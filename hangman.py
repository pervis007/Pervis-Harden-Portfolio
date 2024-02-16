
#The secret word the player is trying to guess
secretWord = "hello"
lettersGuessed = ""

#The number of turns before the player loses
failureCount = 7

#Loop until the player has made too many failed attempts
#Will 'break' loop if they succeed instead
while failureCount > 0:
    
    #Get the guessed letter from the player
    guess = input("Enter a letter: ")

    if guess in secretWord:
        #player guessed a correct letter
        print(f"Correct! {guess} is in the secret word.") 
    else:
        #player guessed wrong 
        failureCount -= 1
        print(f"Incorrect. There are no {guess} in the secret word. {failureCount} turn(s) left")
    #Maintain a list of all letters guessed
    lettersGuessed = lettersGuessed + guess 
    wrongLetterCount = 0

    for letter in secretWord:
        if letter in lettersGuessed:
            print(f"{letter}", end=" ")
        else:
            print("... ",end=" ")
            wrongLetterCount += 1
#If there were no wrong letters, then the player win!
    if wrongLetterCount == 0:
        print(f"Congrats Lame Smart Ah Nigga! The secret word was {secretWord}. You won, dork!")
        break


else:
    print(f"Sorry ya didn't win dumb ah nigga! the word was {secretWord}")