from modules.imports import *



def print_hit_hold() -> None:
    print('-' * 26)
    print('hit   | Бросить кости')
    print('hold  | Остановиться')
    print('-' * 26)


def print_player_overcapped() -> None:
    print('-' * 26)
    print('Игрок перебрал!\nДилер выиграл! Нажмите enter\nчтобы играть заново...')
    print('-' * 26)


def print_dealer_overcapped() -> None:
    print('-' * 26)
    print('Дилер перебрал!\nИгрок выиграл! Нажмите enter\nчтобы играть заново...')
    print('-' * 26)


def print_player_won() -> None:
    print('-' * 26)
    print('Игрок победил!\nНажмите enter чтобы играть заново...')
    print('-' * 26)


def print_dealer_won() -> None:
    print('-' * 26)
    print('Дилер победил!\nНажмите enter чтобы играть заново...')
    print('-' * 26)


def print_draw() -> None:
    print('-' * 26)
    print('Ничья!\nНажмите enter чтобы играть заново...')
    print('-' * 26)


def hit() -> int:
    return randint(1, 11)


def points_counter() -> Generator[int, None, None]:
    counter = 0
    while True:
        cur_hit = hit()
        counter += cur_hit
        yield counter

