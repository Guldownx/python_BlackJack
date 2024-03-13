from modules import *

if __name__ == '__main__':
    while True:
        print('-' * 26)
        print('           21*           ')
        print('-' * 26)
        print('Диллер должен бросать пока\nу него < 17')
        players_points = points_counter()
        dealer_points = points_counter()
        check_player = 0
        check_dealer = 0
        while True:
            if check_player > 21:
                print_player_overcapped()
                break
            if check_player == 21:
                print_player_won()
                break
            print_hit_hold()
            question = input(f'>{check_player} ')
            if question == 'hit':
                check_player = next(players_points)
                print('Игрок*', check_player)
            elif question == 'hold':
                print('Игрок:', check_player)
                break
            else:
                continue
        if check_player < 21:
            while True:
                if check_dealer > 21:
                    print_dealer_overcapped()
                    break
                if check_dealer == 21:
                    print_dealer_won()
                    break
                if check_dealer < 17:
                    check_dealer = next(dealer_points)
                    print('Дилер*', check_dealer)
                else:
                    print('-' * 26)
                    print('Дилер:', check_dealer)
                    print('-' * 26)
                    break
            if check_dealer < 21:
                if check_player > check_dealer:
                    print_player_won()
                elif check_player < check_dealer:
                    print_dealer_won()
                else:
                    print_draw()
        input()



