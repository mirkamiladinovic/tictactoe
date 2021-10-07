"""
gameboard = {'Gore_lijevo':' ', 'Gore_srednje':' ', 'Gore_desno':' ',
              'Srednje_lijevo':' ', 'Srednje_srednje':' ', 'Srednje_desno':' ',
              'Dolje_lijevo':' ', 'Dolje_srednje':' ', 'Dolje_desno':' '}
"""

gameboard = {'GL':' ', 'GS':' ', 'GD':' ',
              'SL':' ', 'SS':' ', 'SD':' ',
              'DL':' ', 'DS':' ', 'DD':' '}

def print_gameboard(gameboard):  
        print('  ', gameboard['GL'], '  |','  ' ,gameboard['GS'], '  |', '  ',gameboard['GD'])
        print('-------+--------+--------')
        print('  ', gameboard['SL'], '  |','  ' ,gameboard['SS'], '  |', '  ',gameboard['SD'])
        print('-------+--------+--------')
        print('  ', gameboard['DL'], '  |','  ' ,gameboard['DS'], '  |', '  ',gameboard['DD'], '\n')

def check_gameboard(gameboard):
    if gameboard['GL'] == gameboard['GS'] == gameboard['GD'] != ' ' or \
        gameboard['GL'] == gameboard['SL'] == gameboard['DL'] != ' ' or \
            gameboard['GS'] == gameboard['SS'] == gameboard['DS'] != ' ' or \
                gameboard['GD'] == gameboard['SD'] == gameboard['DD'] != ' ' or \
                    gameboard['SL'] == gameboard['SS'] == gameboard['SD'] != ' ' or \
                        gameboard['DL'] == gameboard['DS'] == gameboard['DD'] != ' ' or \
                            gameboard['GL'] == gameboard['SS'] == gameboard['DD'] != ' ' or \
                                gameboard['DL'] == gameboard['SS'] == gameboard['GD'] != ' ':
        return True
    else: return False

turn = 'X'
brojac_poteza = 0
game_end = False
print_gameboard(gameboard)
#for i in range 9:
while not game_end:
    print('Na potezu je', turn ,'. Izaberite mjesto')
    move = input()
        
    while gameboard[move] != ' ':
        print("pogresan unos, unesi", turn, "negdje drugo")
        move = input()
    
    gameboard[move] = turn
    brojac_poteza += 1
    print_gameboard(gameboard)

    if check_gameboard(gameboard):
        print('Pobjednik je', turn)
        print_gameboard(gameboard)
        gameboard = {'Gornje_l':' ', 'Gornje_s':' ', 'Gornje_d':' ',
              'Srednje_l':' ', 'Srednje_s':' ', 'Srednje_d':' ',
              'Donje_l':' ', 'Donje_s':' ', 'Donje_d':' '}
        print('Pocinje nova igra')
        print_gameboard(gameboard)
        continue
    elif brojac_poteza == 9:
        print('Draw game')
        gameboard = {'Gornje_l':' ', 'Gornje_s':' ', 'Gornje_d':' ',
              'Srednje_l':' ', 'Srednje_s':' ', 'Srednje_d':' ',
              'Donje_l':' ', 'Donje_s':' ', 'Donje_d':' '}
        print('Pocinje nova igra')
        print_gameboard(gameboard)

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
print_gameboard(gameboard)

