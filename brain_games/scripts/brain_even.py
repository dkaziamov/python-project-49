from brain_games.game_engine import start_game
from brain_games.games.game_logic_brain_even import brain_even


def main():
    start_game(brain_even)


if __name__ == "__main__":
    main()
