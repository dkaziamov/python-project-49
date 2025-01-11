def get_user_answer_int():
    user_answer = input()
    try:
        user_answer = int(user_answer)
        return int(user_answer)
    except ValueError:
        return get_user_answer_int()
    
get_user_answer_int()
