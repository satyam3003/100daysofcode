# -------------hangman-------------------
import random
import hangman_art as ha
import hangman_logo as hl

print(hl.logo)
print("\nHello there!\nLets start the game...\n")
word_list = ["aardvark", "baboon", "camel", "computer", "mouse", 'keyboard', 'pendrive', 'dog', 'rat', 'cat', 'window',
             'river', 'beach', 'bedroom']
selected_word = random.choice(word_list)

check_list = []
for lines in range(len(selected_word)):
    check_list.append("_")
# print(check_list)

inp_word = ''
inp_word2 = ''
lives = 6

while inp_word != selected_word and lives > 0:
    i = 0
    input_word = input('Guess a letter: ').lower()
    inp_word = ''
    inp_word2 = ''
    for letter in selected_word:
        if input_word == letter:
            check_list[i] = letter
        inp_word = inp_word +  check_list[i]
        inp_word2 = inp_word2 + " " + check_list[i]
        i = i + 1

    presence = inp_word.count(input_word)
    if presence == 0:
        lives = lives - 1
        print(f"You guessed {input_word}, which is not in the word. You lose 1 life ")
    print(ha.stages[lives])
    print(f"\t \t \t    {inp_word2} \n\n")

if inp_word == selected_word:
    print("Congratulations you won!")
elif lives == 0:
    print(f"You Lost! correct word is {selected_word}")
