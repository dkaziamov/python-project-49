import prompt

from brain_games.text_data import messages
from brain_games.game_utils import (
    get_user_name,
)


def start_game(game_function):
    target_score = 3  # maximum score required to win the game
    user_score = 0
    print(messages['game_welcome'])
    user_name = get_user_name()
    print(messages['greeting_user'](user_name))

    while user_score < target_score:
        if not game_function(user_name):
            break
        user_score += 1

    if user_score >= target_score:
        print(messages['victory_message'](user_name))
