#This program is practice to create a small game using basic classes

import random

#Creation of a player class for the game
class Player:

    #Constructor for the player
    def __init__(self, name, score, lives):
        self.score = 0 #Score for the game
        self.name = input("What is your name? ") #Name of the player
        self.lives = 3 #Player lives

    #Function to increment the player's score
    def addScore(self):
        self.score = self.score + 1
    
    #Function to decrement the player's lives
    def minusLife(self):
        self.lives = self.lives - 1

#Create the player
newPlayer = Player(name ="", score = 0, lives = 3)
print("\nHello " + newPlayer.name + "! Let's play a game!\n") #Message to the player

#Begin the creation of the game
print("The idea for the game is simple. You (The Player) provide a numerical guess ranging from one to six. \nThe computer rolls a dice, and if your number matches, your score gets raised by one! However, guess wrong three times, and the game ends. Begin!\n") #Message to explain the game
gameRun = True #Variable that indicates whether or not to continue playing

while (gameRun):
    playerGuess = int(input("Please enter an integer ranging from 1-6: ")) #Get the player's guess

    while ((playerGuess != 1) and (playerGuess != 2) and (playerGuess != 3) and (playerGuess != 4) and (playerGuess != 5) and (playerGuess != 6)): #While the guess is not valid, get a new gues
        playerGuess = input("Please enter a valid input ranging from 1-6: ")
    
    targetNumber = random.randint(1,6) #Get the target number

    #Take actions based on the player's guess
    if (playerGuess == targetNumber):
        newPlayer.addScore()
        print("Congratulations! Your guess was correct! Your score is now " + str(newPlayer.score))
    else:
        newPlayer.minusLife()
        print("Oh no! Your guess was incorrect! You now have " + str(newPlayer.lives) + " lives")

    if (newPlayer.lives < 1):
        print("\nLooks like you're out of lives! That's the game. Your final score was " + str(newPlayer.score))
        gameRun = False
