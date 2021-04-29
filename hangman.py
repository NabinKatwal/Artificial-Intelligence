import random

class Hangman:
    def __init__(self):
        self.chance = 6;
        self.guessed = []
        self.wrong = []


    def get_word(self):
        word_list = ['Cat','Luffy','Artificial']
        return random.choice(word_list)

    def difficulty(self):
        pass

    def logic(self):
        word = self.get_word()
        letter_list = [word[i] for i in range(0, len(word))]
        guess_list = ['_' for i in range(0,len(word))]
        for i in letter_list:
            print(i)
            

    def play(self):
        pass 



if __name__ == "__main__":
    hangman = Hangman()

    hangman.logic()