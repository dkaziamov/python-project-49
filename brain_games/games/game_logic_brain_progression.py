def brain_progression(difficulty_level, user_name):
    # print('What number is missing in the progression?')
    correct_answer = create_arithmetic_progression(difficulty_level)

    user_answer = prompt.string('Your answer: ')
    if not is_user_answer_number(user_answer):
        lose_user(user_name, user_answer, correct_answer)
        return False
    user_answer = int(user_answer)
    return is_user_answer_correct(user_name, user_answer, correct_answer)