def brain_even(difficulty_level, user_name):
    # print('Answer "yes" if the number is even, otherwise answer "no".')
    question_number = generate_random_number(difficulty_level)
    print(f'Question: {question_number}')
    correct_answer = if_number_is_even(question_number)

    user_answer = prompt.string('Your answer: ')
    return is_user_answer_correct(user_name, user_answer, correct_answer)