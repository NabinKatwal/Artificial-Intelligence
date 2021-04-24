import random

class Hangman:
    def __init__(self):
        pass

    def get_word(self):
        word_list = ['Cat','Luffy','Artificial']
        return word_list

    def difficulty(self, choice):
        word = self.get_word()
        if choice.lower() == 'easy' and len(word) < 4:
            return random.choice(word)
        elif choice.lower() == 'medium' and 4 <= len(word) <= 8:
            return random.choice(word)
        else:
            return random.choice(word)

    def logic(self, choice):
        word = self.difficulty(choice)
        letter_list = [word[i] for i in range(0, len(word))]
        guess_list = ['_' for i in range(0,len(word))]
        print(word)

    def play(self):
        choice = input("Select difficulty level: 1. Easy 2. Medium 3. Hard ")
        self.logic(choice)



if __name__ == "__main__":
    hangman = Hangman()

    hangman.play()