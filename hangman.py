import random

class Hangman:
    def __init__(self):
        self.chance = 6;
        self.guessed = []
        self.wrong = []
        self.guess_list = []
        self.letter_list = []
        self.level = 1

    def agent(self):
        #TODO Implement simple intelligent agent to solve the missing letters
        pass

    def get_word(self):
        word_list = ['Catfish','Luffy','Artificial']
        return random.choice(word_list).upper()

    def difficulty(self):
        self.level = int(input("Select difficulty level: (1/2/3)->"))
        return self.level

    def logic(self):
        self.difficulty()
        word = self.get_word()
        self.letter_list = [word[i] for i in range(0, len(word))]
        self.guess_list = ['_' for i in range(0,len(word))]
        if self.level == 1:
            word_hint, word_hint1, word_hint2 = random.randint(1, len(self.letter_list)-1), random.randint(1, len(self.letter_list)-1), random.randint(1, len(self.letter_list)-1)
        if self.level == 2:
            word_hint, word_hint1 = random.randint(1, len(self.letter_list)-1), random.randint(1, len(self.letter_list)-1) 
        if self.level == 3:
            word_hint = random.randint(1, len(self.letter_list)-1)
        for i in range(0, len(self.letter_list)):
            if self.level == 1:
                self.guess_list[word_hint] = self.letter_list[word_hint]
                self.guess_list[word_hint1] = self.letter_list[word_hint1]
                self.guess_list[word_hint2] = self.letter_list[word_hint2]
            if self.level == 2:
                self.guess_list[word_hint] = self.letter_list[word_hint]
                self.guess_list[word_hint1] = self.letter_list[word_hint1]
            if self.level == 3:
                self.guess_list[word_hint] = self.letter_list[word_hint]

    def play(self):
        index_alphabet = ''
        self.logic()
        print("HANGMAN")
        print(f"Your word to guess is: {self.guess_list}")
        word = ''
        while self.chance != 0:
            print(f"Progress: {self.guess_list}")
            print(f"Chances left: {self.chance}")
            word = (input("Enter your choice->")).upper()
            print(f"you entered: {word}")
            if word in self.wrong:
                print("You already guessed this letter. This doesn't count.")
                self.chance += 1
            if word in self.letter_list:
                self.guessed.append(word)
                index_alphabet = self.letter_list.index(word)
                if word in self.guess_list:
                    # self.letter_list.remove(index_alphabet)
                    pass
                else:
                    self.guess_list[index_alphabet] = self.letter_list[index_alphabet]
                if '_' not in self.guess_list:
                    print("You won")
                    print(f"The word was {self.get_word()}")
                    break 
            else:
                self.wrong.append(word)
                self.chance -= 1
            if self.chance == 1:
                print("Last Chance. Exiting at next wrong guess.")
            print("\n")
        print(self.guessed)
        print(self.wrong)


if __name__ == "__main__":
    hangman = Hangman()
    # hangman.logic()
    hangman.play()