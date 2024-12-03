import random


class GameLogic:
    def __init__(self, words):
        self.words = words
        self.current_word = None

    def start_new_game(self):
        if not self.words:
            return None
        self.current_word = random.choice(self.words)
        self.words.remove(self.current_word)
        return ["■"] * len(self.current_word)

    def make_guess(self, guess, hidden_word):
        if len(guess) == 1 and guess.isalpha():
            if guess in self.current_word:
                new_hidden_word = list(hidden_word)
                for i, letter in enumerate(self.current_word):
                    if letter == guess:
                        new_hidden_word[i] = guess
                return "".join(new_hidden_word)
            else:
                return False
        elif len(guess) == len(self.current_word) and guess.isalpha():
            return self.current_word
        else:
            return False

    def game_over(self, hidden_word):
        return "".join(hidden_word) == self.current_word

    def get_word(self):
        return self.current_word
