from modules.file_manager import FileManager
from modules.game_logic import GameLogic


file_manager = FileManager()
words = file_manager.load_words()
record = file_manager.load_record()
game = GameLogic(words)

while True:
    hidden_word = game.start_new_game()
    if hidden_word is None:
        print("Список слов пуст. Завершение игры.")
        break

    difficulty = input("Выберите уровень сложности (легкий, средний, сложный): ").lower()
    if difficulty == "легкий":
        lives = 7
    elif difficulty == "средний":
        lives = 5
    elif difficulty == "сложный":
        lives = 3
    else:
        print("Неверный уровень сложности. Игра будет запущена на легком уровне.")
        lives = 7

    print("Угадайте слово:", "".join(hidden_word))

    while lives > 0 and not game.game_over(hidden_word):
        try:
            guess = input("Введите букву или слово целиком: ").upper()
            result = game.make_guess(guess, hidden_word)
            if result is False:
                lives -= 1
                print(f"Неверно. Осталось {lives} жизней.")
            elif isinstance(result, str):
                hidden_word = result
                print(hidden_word)

        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

        if game.game_over(hidden_word):
            print(f"Вы угадали слово {game.get_word()}!")
            record += 1
            file_manager.save_record(record)
            break

        if not game.words:
            print("Все слова угаданы!")
            break

    if lives == 0:
        print(f'Ваш счёт: {record}. Игра окончена!')
        exit()
    else:
        print(f"Ваш счёт: {record}")
        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if play_again == 'нет':
            print('Игра окончена!')
            exit()
