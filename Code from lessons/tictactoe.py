
def displayGrid(info):
    print('   0 1 2')
    print('   _ _ _ ')
    print('  |' + info[0][0] + '|' + info[0][1] + '|' + info[0][2] + '|')
    print('0 |_|_|_|')
    print('  |' + info[1][0] + '|' + info[1][1] + '|' + info[1][2] + '|')
    print('1 |_|_|_|')
    print('  |' + info[2][0] + '|' + info[2][1] + '|' + info[2][2] + '|')
    print('2 |_|_|_|')

def gameOver(info):
    if ('X' == info[0][0] and 'X' == info[0][1] and 'X' == info[0][2]) or ('X' == info[0][0] and 'X' == info[1][1] and 'X' == info[2][2]) or ('X' == info[0][0] and 'X' == info[1][0] and 'X' == info[2][0]) or ('X' == info[1][0] and 'X' == info[1][1] and 'X' == info[1][2]) or ('X' == info[2][0] and 'X' == info[1][1] and 'X' == info[0][2]) or ('X' == info[1][1] and 'X' == info[2][1] and 'X' == info[0][1]) or ('X' == info[1][2] and 'X' == info[2][2] and 'X' == info[0][2]):
        print("Player 1 wins! Game over.")
        displayGrid(info)
        return 1
    elif ('O' == info[0][0] and 'O' == info[0][1] and 'O' == info[0][2]) or ('O' == info[0][0] and 'O' == info[1][1] and 'O' == info[2][2]) or ('O' == info[0][0] and 'O' == info[1][0] and 'O' == info[2][0]) or ('O' == info[1][0] and 'O' == info[1][1] and 'O' == info[1][2]) or ('O' == info[2][0] and 'O' == info[1][1] and 'O' == info[0][2]) or ('O' == info[1][1] and 'O' == info[2][1] and 'O' == info[0][1]) or ('O' == info[1][2] and 'O' == info[2][2] and 'O' == info[0][2]):
        print("Player 2 wins! Game over.")
        displayGrid(info)
        return 1
    for row in info:
        for val in row:
            if val != ' ':
                return 0    
    displayGrid(info)
    print('Tie. Game over.')
    return 1

def game(info):
    moves = 1
    chars = {1: "X", 2: "O"}
    while moves <= 9:
        if moves % 2 == 1:
            player = 1
        elif moves % 2 == 0:
            player = 2
        coords = input("Player " + str(player) + " make your move: ")
        row = int(coords[0])
        col = int(coords[2])
        if info[row][col] == ' ':
            info[row][col] = chars[player]
        if gameOver(info) == 1:
            return
        displayGrid(info)
            
        
        



        # process the input

        # check if the move is valid

        # update list, call displaygrid

        # check if player has 3 in a row


    


        moves = moves + 1





if __name__ == "__main__":
    info = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    displayGrid(info)
    game(info)

    # Use the input() function to take in the choices of each player
    # ex: coordinates = input("Player 1, which coordinates would you like to place an X?")
    # Remember that all input comes in strings, use int() to convert to an integer
    # Check the array each move to see if there is a 3 in a row
    # Check the array to make sure each inputted coordinate is not already occupied






# Tic Tac Toe
# 2 players
# players take turns, one after the other
# 3x3 grid
# X's and O's
# Choose a space that hasn't already been chosen
# Aim is to get 3 in a row - vertical, horizontal, or diagonal
# Game ends when a player wins or all spaces are filled

# Code considerations
# need to get input (can assume both players on same computer)
# need to display the grid
# need to track whose turn it is
# need to determine if chosen space is open
# need to check if the game is over/if a player has won
# need to repeat this process if game not over

