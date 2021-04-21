import random

class Hangman:
    def __init__(self):
        pass

    def get_word(self):
        word_list = ['Hello','Luffy','Artificial']
        return random.choice(word_list)

    def logic(self):
        word = self.get_word()
        letter_list = [word[i] for i in range(0, len(word))]
        guess_list = ['_' for i in range(0,len(word))]
        temp = [letter_list, guess_list]
        playing_list = []
        for i in range(0,len(word)):
            playing_list.append(random.choice(random.choices(temp, weights=map(len, temp))[0]))
        print(letter_list)
        print(guess_list)
        print(playing_list)



if __name__ == "__main__":
    hangman = Hangman()

    hangman.logic()