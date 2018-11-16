grid = [[2, 0, 1],
        [0, 2, 0],
        [1, 2, 2]]


def display_game(game_grid):
    print("   0  1  2")
    for count, row in enumerate(game_grid):
        print(count, row)
        

def game_moves(game_grid, player=0, row=0, column=0):
    if player != 0:
        game_grid[row][column] = player
    return game_grid


def check_winner(check_list):
    if check_list.count(check_list[0]) == len(check_list) and check_list[0] != 0:
            print("Congratulations, The winner is: ", check_list[0])


def identify_Winner(game_grid):
    #horizontal winner
    for row in game_grid:
        check_winner(row)
    
    #vertical winner
    for cols in range(len(game_grid)):
        vertical=[]
        for row in game_grid:
            vertical.append(row[cols])
        check_winner(vertical)
    
    # forward diagnoal winner
    forward_diag = []
    for index in range(len(game_grid)):
        forward_diag.append(game_grid[index][index])
    check_winner(forward_diag)
    
    #backward diagonal winner
    backward_diag = []
    for row, col in enumerate(reversed(range(len(game_grid)))):
        backward_diag.append(game_grid[row][col])
    check_winner(backward_diag)


display_game(grid)
identify_Winner(grid)
grid = game_moves(grid, 2, 2, 0)
