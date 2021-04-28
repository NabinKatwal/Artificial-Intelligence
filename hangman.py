import random

class Hangman:
    def __init__(self):
        pass

    def get_word(self):
        word_list = ['Cat','Luffy','Artificial']
        return random.choice(word_list)

    def difficulty(self):
        pass

    def logic(self, choice):
        word = self.get_word()
        letter_list = [word[i] for i in range(0, len(word))]
        guess_list = ['_' for i in range(0,len(word))]
        print(word)

    def play(self):
        pass 



if __name__ == "__main__":
    hangman = Hangman()

    hangman.play()