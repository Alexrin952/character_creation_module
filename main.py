from random import randint


def attack(char_name: str, char_class: str) -> str:
    """
    Вычисляет урон, наносимый персонажем в зависимости от его класса.

    :param char_name: Имя персонажа.
    :param char_class: Класс персонажа.
    :return: Сообщение с результатом атаки.
    """
    damage = {
        'warrior': randint(3, 5),
        'mage': randint(5, 10),
        'healer': randint(-3, -1),
    }
    message = f'{char_name} нанёс урон противнику '
    message += f'равный {5 + damage.get(char_class, 0)}'
    return message


def defence(char_name: str, char_class: str) -> str:
    """
    Вычисляет блокированный урон персонажем в зависимости от его класса.

    :param char_name: Имя персонажа.
    :param char_class: Класс персонажа.
    :return: Сообщение с результатом блокирования урона.
    """
    block = {
        'warrior': randint(5, 10),
        'mage': randint(-2, 2),
        'healer': randint(2, 5),
    }
    return f'{char_name} блокировал {10 + block.get(char_class, 0)} урона'


def special(char_name: str, char_class: str) -> str:
    """
    Выполняет специальное действие персонажа в зависимости от его класса.

    :param char_name: Имя персонажа.
    :param char_class: Класс персонажа.
    :return: Сообщение с результатом выполнения специального действия.
    """
    specials = {
        'warrior': 'Выносливость',
        'mage': 'Атака',
        'healer': 'Защита',
    }
    values = {
        'warrior': 105,
        'mage': 45,
        'healer': 40,
    }
    message = f'{char_name} применил специальное умение '
    message += f'«{specials.get(char_class, "")} {values.get(char_class, 0)}»'
    return message


def start_training(char_name: str, char_class: str) -> str:
    """
    Запускает тренировку персонажа, позволяя пользователю вводить команды.

    :param char_name: Имя персонажа.
    :param char_class: Класс персонажа.
    :return: Сообщение об окончании тренировки.
    """
    class_desc = {
        'warrior': 'Воитель — отличный боец ближнего боя.',
        'mage': 'Маг — превосходный укротитель стихий.',
        'healer': 'Лекарь — чародей, способный исцелять раны.',
    }
    print(f"""
{char_name}, ты {class_desc.get(char_class, "Неизвестный класс")}
Потренируйся управлять своими навыками.
Введи одну из команд: attack — чтобы атаковать,
defence — чтобы блокировать атаку, special — чтобы использовать суперсилу.
Если не хочешь тренироваться, введи команду skip.
""")
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        elif cmd == 'defence':
            print(defence(char_name, char_class))
        elif cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """
    Позволяет пользователю выбрать класс персонажа.

    :return: Выбранный пользователем класс персонажа.
    """
    class_desc = {
        'warrior': ('Воитель — дерзкий воин ближнего боя. '
                    'Сильный, выносливый и отважный.'),
        'mage': ('Маг — находчивый'
                 'воин дальнего боя.'
                 'Обладает высоким интеллектом.'),
        'healer': ('Лекарь — могущественный заклинатель. '
                   'Черпает силы из природы, веры и духов.'),
    }
    approve_choice: str = ''
    char_class: str = ''  # Инициализация пустой строкой
    while approve_choice != 'y':
        char_class = input(
            'Выбери класс: Воитель — warrior, Маг — mage, Лекарь — healer: ',
        )
        print(class_desc.get(char_class, 'Неизвестный класс'))
        approve_choice = input(
            'Нажми (Y), чтобы подтвердить выбор,\n'
            'или любую другую кнопку, чтобы выбрать другого персонажа\n',
        ).lower()
    return char_class



if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class)) 
