STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.maskedWord = '_' * len(word)
        self.previousGuesses = set()

    def guess(self, char):
        if self.remaining_guesses < 0:
            raise ValueError('No remaining guesses!')
        if self.status == STATUS_WIN:
            raise ValueError('You already won the game!')
        isSuccessfulGuess = False
        if char not in self.previousGuesses:
            self.previousGuesses.add(char)
            for i in range(len(self.word)):
                if char == self.word[i]:
                    maskedWordCharList = list(self.maskedWord)
                    maskedWordCharList[i] = char
                    self.maskedWord = ''.join(maskedWordCharList)
                    isSuccessfulGuess = True
            if self.maskedWord == self.word:
                self.status = STATUS_WIN
        if isSuccessfulGuess == False:
            self.remaining_guesses-= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE
            else:
                self.status = STATUS_ONGOING

    def get_masked_word(self):
        return self.maskedWord

    def get_status(self):
        return self.status