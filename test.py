from word_pick import word_pick

def word_check(rand_word, user_word, try_no):
    if rand_word == user_word:
        print(f'Match: ✓✓✓✓✓')
        print(f'You Won the Game in {try_no} tries')
        exit()
    else:
        feedback = []
        for i in range(5):
            if user_word[i] == rand_word[i]:
                feedback.append(user_word[i])
            else:
                feedback.append("_")
    return " ".join(feedback)

# my_list = ['HELLO', 'AUDIO', 'POEMS', 'FOYER', 'ROMEO']
rand_word = word_pick()
print(rand_word)

for choice in range(5):
    print(f'Turn {choice+1}:')
    print('------------')
    
    while True: 
        user_input = input( ).strip().upper()
        if len(user_input) == 5:
            break
        else:
            print("Invalid input! Please enter exactly 5 letters.")
    print('------------')

    print(f'Entry{choice+1}: {user_input}')
    result = word_check(rand_word, user_input, choice+1)
    print(f'result:{result}')
    if choice == 4:
        print('XXXXXXXXXXX')
        print('X         X')
        print(f'X  {rand_word}  X')
        print('X         X')
        print('XXXXXXXXXXX')
    print('************')
