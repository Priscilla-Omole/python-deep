print('*' * 10)

username = input('Enter your username: ')
password = input('Enter your password: ')

password_length = len(password)

hidden_password = '*' * password_length

print(f"Your password, {hidden_password} is {len(password)} characters long.")