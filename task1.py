import random

# Categories
fruits = ["apple", "mango", "banana", "orange", "grapes"]
animals = ["tiger", "lion", "rabbit", "monkey", "elephant"]
programming = ["python", "java", "coding", "computer", "html"]

print("===== Hangman Game =====")
print("Choose a Category:")
print("1. Fruits")
print("2. Animals")
print("3. Programming")

choice = input("Enter your choice (1/2/3): ")

# Select category
if choice == "1":
    word = random.choice(fruits)
    print("\nCategory: Fruits")
elif choice == "2":
    word = random.choice(animals)
    print("\nCategory: Animals")
elif choice == "3":
    word = random.choice(programming)
    print("\nCategory: Programming")
else:
    print("Invalid Choice!")
    exit()

guessed = []
chances = 6

while chances > 0:
    display = ""

    # Show guessed letters
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check win
    if "_" not in display:
        print(" You Won")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("You already guessed this letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct")
    else:
        chances -= 1
        print(" Wrong")
        print("Remaining Chances:", chances)

if chances == 0:
    print("\n💀 Game Over!")
    print("Correct Word:", word)