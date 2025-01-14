import prompt


def start_game(game_function) -> None:
    target_score = 3  # maximum score required to win the game
    user_score = 0  # default user score
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    while user_score < target_score:
        task_message, task_question, correct_answer = game_function()
        print(task_message)
        print(f"Question: {task_question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
            user_score += 1
        else:
            print(f'"{user_answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}".')
            print(f"Let's try again, {user_name}!")
            break
    if user_score >= target_score:
        print(f"Congratulations, {user_name}!")
