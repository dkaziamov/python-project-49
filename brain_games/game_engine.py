import prompt


def start_game(game_function) -> None:
    target_score = 3  # maximum score required to win the game
    user_score = 0  # default user score
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    while user_score < target_score:
        if not game_function():
            print(f"Let's try again, {user_name}!")
            break
        user_score += 1
    if user_score >= target_score:
        print(f"Congratulations, {user_name}!")


def play_round(
        task_message,
        task_question,
        correct_answer,
) -> bool:
    print(task_message)
    print(f"Question: {task_question}")
    user_answer = prompt.string("Your answer: ")
    if user_answer == correct_answer:
        print("Correct!")
        return True
    print(f'"{user_answer}" is wrong answer ;(. '
          f'Correct answer was "{correct_answer}".')
    return False
