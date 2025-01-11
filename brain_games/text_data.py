messages = {
    'game_welcome': 'Welcome to the Brain Games!',
    'user_name': 'May I have your name? ',
    'question_display': 'Question:',
    'feedback_correct': 'Correct!',
    'task_missing_number': 'What number is missing in the progression?',
    'task_expression_result': 'What is the result of the expression?',
    'task_gcd': 'Find the greatest common divisor of given numbers.',
    'task_even_number':
        'Answer "yes" if the number is even, otherwise answer "no".',
    'task_prime_number':
        'Answer "yes" if given number is prime. Otherwise answer "no".',
    'feedback_try_again': lambda user_name: f"Let's try again, {user_name}!",
    'greeting_user': lambda user_name: f'Hello, {user_name}!',
    'victory_message': lambda user_name: f'Congratulations, {user_name}!',
    'feedback_wrong_answer': lambda user_answer, correct_answer: (
        f'"{user_answer}" is wrong answer ;(.'
        f' Correct answer was "{correct_answer}".'
    )
}
