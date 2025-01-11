from brain_games.text_data import messages
from brain_games.game_utils import (
    generate_random_number,
    convert_bool_to_yes_no,
    is_user_answer_correct,
    if_number_is_even,
    get_user_answer,
    feedback_result
)


def brain_even(user_name):
    DIFFICULTY_LEVEL = 10  # sets the max number for generate_random_number()
    print(messages['task_even_number'])
    question_number = generate_random_number(DIFFICULTY_LEVEL)
    print(f"{messages['question_display']} {question_number}")
    correct_answer_bool = if_number_is_even(question_number)
    correct_answer_str = convert_bool_to_yes_no(correct_answer_bool)
    user_answer_str = get_user_answer()
    result = is_user_answer_correct(user_answer_str, correct_answer_str)
    return feedback_result(
        result, user_name, user_answer_str, correct_answer_str
    )
