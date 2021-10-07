gameboard = {'1':' ', '2':' ', '3':' ', '4':' ',
              '5':' ', '6':' ', '7':' ', '8':' ',
              '9':' ', '10':' ', '11':' ', '12':' ',
              '13':' ', '14':' ', '15':' ', '16':' ',}

def print_gameboard(gameboard):  
        print('  ', gameboard['1'], '  |','  ' , gameboard['2'], '  |', '  ', gameboard['3'], '  |', gameboard['4'])
        print('-------+--------+--------+--------')
        print('  ', gameboard['5'], '  |','  ' , gameboard['6'], '  |', '  ', gameboard['7'], '  |', gameboard['8'])
        print('-------+--------+--------+--------')
        print('  ', gameboard['9'], '  |','  ' , gameboard['10'], '  |', '  ', gameboard['11'], '  |', gameboard['12'])
        print('-------+--------+--------+--------')
        print('  ', gameboard['13'], '  |','  ' , gameboard['14'], '  |', '  ', gameboard['15'], '  |', gameboard['16'], '\n')
 
def check_gameboard(gameboard):
    if gameboard['1'] == gameboard['2'] == gameboard['3'] == gameboard['4'] != ' ' or \
        gameboard['5'] == gameboard['6'] == gameboard['7'] == gameboard['8'] != ' ' or \
            gameboard['9'] == gameboard['10'] == gameboard['11'] == gameboard['12'] != ' ' or \
                gameboard['13'] == gameboard['14'] == gameboard['15'] == gameboard['16'] != ' ' or \
                    gameboard['1'] == gameboard['5'] == gameboard['9'] == gameboard['13'] != ' ' or \
                        gameboard['2'] == gameboard['6'] == gameboard['10'] == gameboard['14'] != ' ' or \
                            gameboard['3'] == gameboard['7'] == gameboard['11'] == gameboard['15'] != ' ' or \
                                gameboard['4'] == gameboard['8'] == gameboard['12'] == gameboard['16'] != ' ' or \
                                    gameboard['1'] == gameboard['6'] == gameboard['11'] == gameboard['16'] != ' ' or \
                                        gameboard['13'] == gameboard['10'] == gameboard['7'] == gameboard['4'] != ' ' :
                                    
        return True
    else: return False

turn = 'X'
brojac_poteza = 0

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
        gameboard = {'1':' ', '2':' ', '3':' ', '4':' ',
              '5':' ', '6':' ', '7':' ', '8':' ',
              '9':' ', '10':' ', '11':' ', '12':' ',
              '13':' ', '14':' ', '15':' ', '16':' ',}
        print('Pocinje nova igra')
        print_gameboard(gameboard)
        continue
    elif brojac_poteza == 16:
        print('Draw game')
        gameboard = {'1':' ', '2':' ', '3':' ', '4':' ',
              '5':' ', '6':' ', '7':' ', '8':' ',
              '9':' ', '10':' ', '11':' ', '12':' ',
              '13':' ', '14':' ', '15':' ', '16':' ',}
        print('Pocinje nova igra')
        print_gameboard(gameboard)

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
print_gameboard(gameboard)
