messages = {
    'welcome': 'Welcome to the Brain Games!',
    'welcome_user': lambda user_name: f'Hello, {user_name}!',
    'victory_user': lambda user_name: f'Congratulations, {user_name}!',
    'wrong_answer': lambda user_answer, correct_answer: (
        f'"{user_answer}" is wrong answer ;(.'
        f' Correct answer was "{correct_answer}".'
    )
}

user_name = 'Biba'
print(messages['welcome_user'](user_name))