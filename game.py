class GameManager:# for use with hangman game
    def __init__(self, word, lives, is_playing, display, old_guesses):
        self.word = word
        self.lives = lives
        self.is_playing = is_playing
        self.display = []
        self.old_guesses = []