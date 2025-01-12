from brain_games.game_engine import play_round
from brain_games.game_utils import generate_random_number

DIFFICULTY_LEVEL = 10  # sets the max number for generate_random_number()


def brain_even():
    task_message = 'Answer "yes" if the number is even, otherwise answer "no".'
    question_number = generate_random_number(DIFFICULTY_LEVEL)
    correct_answer = 'yes' if question_number % 2 == 0 else 'no'
    return play_round(
        task_message=task_message,
        task_question=question_number,
        correct_answer=correct_answer,
    )

# def brain_even(user_name: str) -> bool:
#     print(messages['task_even_number'])
#     question_number = generate_random_number(DIFFICULTY_LEVEL)
#     print(f"{messages['question_display']} {question_number}")
#     correct_answer_bool = if_number_is_even(question_number)
#     correct_answer_str = convert_bool_to_yes_no(correct_answer_bool)
#     user_answer_str = get_user_answer()
#     result = compare_answer(user_answer_str, correct_answer_str)
#     return feedback_result(
#         result, user_name, user_answer_str, correct_answer_str
#     )
