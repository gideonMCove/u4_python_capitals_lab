from capitals import states
import random

def capitals_game():
    random.shuffle(states)
    total = 0    
    correct = 0
    incorrect =0

    print('Guess the capitals, see your score out of 50')

    for state in states:
        state_name = state["name"]
        state_capital = state['capital']
        state_guess = input(f"What is the capital of {state_name}").strip()
        print('state guess', state_guess)

        if state_guess.lower() != state_capital.lower():
            total = total + 1
            incorrect = incorrect + 1
            print(f"Incorrect, the state capital is {state_capital}")
            print(f"Score: {correct}/{total}")
        else :
            total = total + 1
            correct = correct + 1
            print(f"Correct!")
            print(f'Score: {correct}/{total}')

        if total == 50:
            print(f"Game over! you scored {total}, and you missed {incorrect}out of {total}")
            replay = input('replay? [y/n]')
            if replay == 'y':
                capitals_game()

capitals_game()   
print(states)
