"""Hangman CLI Word Game.

Features ASCII gallows stage updates, secret word selection from a comprehensive vocabulary,
letter guess tracking, and remaining life counts.
"""

import random
from typing import List, Set

STAGES: List[str] = [
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

LOGO = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

WORD_LIST: List[str] = [
    'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward',
    'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper',
    'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful',
    'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords',
    'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle',
    'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle',
    'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable',
    'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled',
    'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo',
    'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip',
    'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox',
    'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk',
    'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey',
    'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo',
    'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch',
    'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury',
    'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic',
    'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph',
    'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm',
    'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy',
    'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes',
    'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps',
    'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff',
    'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway',
    'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript',
    'transgress', 'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown',
    'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo',
    'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy',
    'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy',
    'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone',
    'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag',
    'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie'
]


def play_hangman() -> None:
    """Execute a single interactive session of Hangman."""
    print(LOGO)
    chosen_word = random.choice(WORD_LIST)
    word_length = len(chosen_word)
    lives = 6
    guessed_letters: Set[str] = set()

    game_over = False

    print(f"\nWord to guess: {'_ ' * word_length}")
    print(STAGES[lives])

    while not game_over:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid alphabetic letter.")
            continue

        if guess in guessed_letters:
            print(f"You have already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed '{guess}'. That is not in the word. You lost a life!")
            if lives == 0:
                game_over = True
                print(f"\n*********************** YOU LOSE ***********************")
                print(f"The correct word was: {chosen_word}")
        else:
            print(f"Good guess! '{guess}' is in the word.")

        display = "".join([letter if letter in guessed_letters else "_" for letter in chosen_word])
        print(f"\nCurrent word state: {' '.join(display)}")

        if "_" not in display:
            game_over = True
            print("\n**************************** YOU WIN! ****************************")

        print(STAGES[lives])


if __name__ == "__main__":
    play_hangman()