import random

lowerLimit = 1
upperLimit = 1000
yesOptions = ['Y', 'y', 'Yes', 'yes', 'YES']
noOptions = ['N', 'n', 'No', 'no', 'NO']
startOptions = ['s', 'start']
customizeOptions = ['c', 'customize']
quitOptions = ['q', 'quit']
highScore = 0
print(highScore)
repeat = True

initialMessage = (f'Guess the correct number in the range {lowerLimit} - {upperLimit}.\n')
print(f'{'_'*len(initialMessage)}\n' + 
      f'\n{' '*int(len(initialMessage)/4)}NUMBER GUESSING GAME')

while (repeat):
    print('\ns - Start\n'+
          'c - Customize range (Default: 1 - 1000)\n'+
          'q - Quit')
    menuInput = (input('Select the option: ')).lower()

    # Handling menu options
    if (menuInput in startOptions):
        pass
    
    elif (menuInput in customizeOptions):
        try:
            lowerLimit = input('Enter new lower limit (Leave empty to use default): ')
            if (lowerLimit.strip() == ''):
                lowerLimit = 1
            else:
                lowerLimit = int(lowerLimit)
        except ValueError:
            print(f'Invalid lower limit. Lower limit set to default {lowerLimit}.')
        
        try:
            upperLimit = input('Enter new upper limit (Leave empty to use default): ')
            if (upperLimit.strip() == ''):
                upperLimit = 1
            else:
                upperLimit = int(upperLimit)
        except ValueError:
            print(f'Invalid upper limit. Lower limit set to default {upperLimit}.')

    elif (menuInput in quitOptions):
        break

    else:
        print('Invalid option. Starting the game...')

    print(f'\nGuess the correct number in the range {lowerLimit} - {upperLimit}.\n' +
        'NOTE - You can skip by giving -1 input.\n')



    # Generate a random number between the specified range.
    number = str(random.randint(lowerLimit, upperLimit))
    userInput = input('Enter the number: ')
    turns = 1

    while (userInput != number):

        # Handle invalid inputs.
        try:
            num = int(userInput)
            if (num != -1):
                if (num < lowerLimit or num > upperLimit):
                    # If input number is not in range.
                    print(f'Invalid number.\n(Number should be in the range {lowerLimit} - {upperLimit}.)\n')
                    userInput = input('Enter the number: ')
                    continue
        except ValueError:
            # If input is not a number.
            print('Invalid input.')
            userInput = input('Enter the number: ')
            continue

        # User can give -1 in the input to skip this number guess.
        if (userInput == '-1'):
            skip = input('Are you sure you want to skip? (Y/N) ')
            # If the user skips, then it will get out of this while loop.
            if (skip in yesOptions):
                turns = 0
                break
            elif (not skip in noOptions):
                print('Invalid input.')

        # Compare the user input with answer and respond accordingly.
        elif (userInput < number):
            print('Too low')

        elif (userInput > number):
            print('Too high')

        # After passing from if...else conditions it will update the user input and increment the 'turns' by 1.
        userInput = input('Enter the number: ')
        turns += 1

    if (turns > 0):
        print(f'\nYou guessed it right in {turns} turns. The number is {number}.')
    else:
        print(f'\nThe number was {int(number)}.')

    repeat = input('Want to play again? (Y/N) ')
    if (repeat in noOptions):
        repeat = False
        highScore = 0
        print(f'{'_'*len(initialMessage)}\n')