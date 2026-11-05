#Errors in Python
'''
So many errors- TypeError, SyntaxError, ValueError, NameError,IndexError,
'''
while True:
    try:
        age = int(input('Enter age: '))
        print(age)
    except (ValueError, ZeroDivisionError) as err:
        print(f'Invalid input {err}')
    else:
        break
    finally:
        print('ok, I am finally done')