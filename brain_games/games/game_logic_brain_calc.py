def brain_calc(difficulty_level, user_name):
    # print('What is the result of the expression?')
    first_number = generate_random_number(difficulty_level)
    second_number = generate_random_number(difficulty_level)
    math_symbol = generate_random_math_symbol()
    print(f'Question: {first_number} {math_symbol} {second_number}')
    correct_answer = math_symbol_to_math_operation(math_symbol)(
        first_number, second_number
    )

    user_answer = prompt.string('Your answer: ')
    if not is_user_answer_number(user_answer):
        lose_user(user_name, user_answer, correct_answer)
        return False
    user_answer = int(user_answer)
    return is_user_answer_correct(user_name, user_answer, correct_answer)