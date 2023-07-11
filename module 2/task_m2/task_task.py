initial_pin = '1234'
n = 0
max_tries = 3
while n < max_tries:

    user_pin = input('Enter your pin: ')
    if len(user_pin) >= 4:
        if initial_pin == user_pin:
            amount = input('How much: ')
            print(f'Take amount {amount}')
            break
        else:
            print('Wrong pin. Try again')
            print(f'You have {max_tries - n-1} tries')
    else:
        print('Pin should be 4 or 6 digits')
    n += 1
print('Good Bye')
