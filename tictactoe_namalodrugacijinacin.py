gameboard = {'Gornje_l':' ', 'Gornje_s':' ', 'Gornje_d':' ',
              'Srednje_l':' ', 'Srednje_s':' ', 'Srednje_d':' ',
              'Donje_l':' ', 'Donje_s':' ', 'Donje_d':' '}

def print_gameboard(gameboard):  
        print('  ', gameboard['Gornje_l'], '  |','  ' ,gameboard['Gornje_s'], '  |', '  ',gameboard['Gornje_d'])
        print('-------+--------+--------')
        print('  ', gameboard['Srednje_l'], '  |','  ' ,gameboard['Srednje_s'], '  |', '  ',gameboard['Srednje_d'])
        print('-------+--------+--------')
        print('  ', gameboard['Donje_l'], '  |','  ' ,gameboard['Donje_s'], '  |', '  ',gameboard['Donje_d'], '\n')

def check_gameboard(gameboard):
    if gameboard['Gornje_l'] == gameboard['Gornje_s'] == gameboard['Gornje_d'] != ' ' or \
        gameboard['Gornje_l'] == gameboard['Srednje_l'] == gameboard['Donje_l'] != ' ' or \
            gameboard['Gornje_s'] == gameboard['Srednje_s'] == gameboard['Donje_s'] != ' ' or \
                gameboard['Gornje_d'] == gameboard['Srednje_d'] == gameboard['Donje_d'] != ' ' or \
                    gameboard['Srednje_l'] == gameboard['Srednje_s'] == gameboard['Srednje_d'] != ' ' or \
                        gameboard['Donje_l'] == gameboard['Donje_s'] == gameboard['Donje_d'] != ' ' or \
                            gameboard['Gornje_l'] == gameboard['Srednje_s'] == gameboard['Donje_d'] != ' ' or \
                                gameboard['Donje_l'] == gameboard['Srednje_s'] == gameboard['Gornje_d'] != ' ':
        return True
    else: return False

"""
def restart_gameboard():
    gameboard = {'Gornje_l':' ', 'Gornje_s':' ', 'Gornje_d':' ',
              'Srednje_l':' ', 'Srednje_s':' ', 'Srednje_d':' ',
              'Donje_l':' ', 'Donje_s':' ', 'Donje_d':' '}
"""

turn = 'X'
brojac_poteza = 0
#for i in range(9):
game_end = False
print_gameboard(gameboard)

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


"""
def igra(gameboard):
    node = "X"
    for i in range(9):
        unos()
        print_gameboard(gameboard)
        print('igrac ', node, 'je na potezu \n')
        turn = input()
        while True:
            if gameboard[turn] == ' ':
                gameboard[turn] = node
                break
            else:
                print("pogresan unos, unesi", node, "negdje drugo \n")
                unos()
                print_gameboard(gameboard)
                turn = input()
        
        provjera = check_gameboard(gameboard)
        if provjera == 1:
            print('Pobjednik je', node)
            break
        else:
            print("Nerijeseno je, nema pobjednika")

        if node == 'X':
            node = 'O'
        else:
            node = 'X'

igra(gameboard)
print_gameboard(gameboard)

"""