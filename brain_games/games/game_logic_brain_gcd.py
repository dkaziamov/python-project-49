def brain_gcd(difficulty_level, user_name):
    # print('Find the greatest common divisor of given numbers.')
    first_number = generate_random_number(difficulty_level)
    second_number = generate_random_number(difficulty_level)
    print(f'Question: {first_number} {second_number}')
    correct_answer = find_gcd(first_number, second_number)

    user_answer = prompt.string('Your answer: ')
    if not is_user_answer_number(user_answer):
        lose_user(user_name, user_answer, correct_answer)
        return False
    user_answer = int(user_answer)
    return is_user_answer_correct(user_name, user_answer, correct_answer)