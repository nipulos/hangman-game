# hangman game
import random

def hangman():
    word_bank = [
        ("tasty", "icecream"),
        ("hot", "coffee"),
        ("cold", "winter"),
        ("bright", "sunshine"),
        ("fast", "car"),
        ("spicy", "tacos"),
        ("sweet", "chocolate"),
        ("warm", "blanket"),
        ("fresh", "bread"),
        ("blue", "ocean"),
        ("night", "sky"),
        ("heavy", "rain"),
        ("soft", "pillow"),
        ("loud", "music"),
        ("funny", "movie"),
        ("happy", "smile"),
        ("lazy", "sunday"),
        ("sharp", "knife"),
        ("cool", "breeze"),
        ("strong", "coffee"),
        ("salty", "fries"),
        ("crispy", "chicken"),
        ("icy", "wind"),
        ("golden", "sunset"),
        ("fluffy", "clouds"),
        ("quiet", "library"),
        ("busy", "street"),
        ("early", "morning"),
        ("late", "night"),
        ("dark", "chocolate"),
        ("fresh", "air"),
        ("smooth", "jazz"),
        ("classic", "movie"),
        ("deep", "sleep"),
        ("warm", "sunlight"),
        ("spinning", "wheels"),
        ("broken", "record"),
        ("electric", "guitar"),
        ("wild", "adventure"),
        ("open", "road"),
        ("calm", "waters"),
        ("rolling", "hills"),
        ("burning", "fire"),
        ("falling", "snow"),
        ("leaking", "faucet"),
        ("rising", "sun"),
        ("clear", "skies"),
        ("hidden", "treasure"),
        ("silver", "moon")
    ]

    word1, word2 = random.choice(word_bank)
    phrase = word1 + " " + word2
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print("Welcome to Hangman!")
    print(f"The phrase has {len(word1)} letters, a space, then {len(word2)} letters.")
    
    while wrong_guesses < max_wrong:
        display = ""
        for char in phrase:
            if char == " ":
                display += " "
            elif char in guessed_letters:
                display += char
            else:
                display += "_"

        print("\nPhrase:", display)
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess ONE letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in phrase:
            wrong_guesses += 1
            print("Wrong")
        else:
            print("Correct")

        if "_" not in display:
            print("You did it")
            print("The phrase was:", phrase)
            return

    print("\n You lost")
    print("The phrase was:", phrase)

hangman()

#i was having trouble running the code on here but it was working on visual studio just fine. if you're having that same problem I can try to fix it if needed