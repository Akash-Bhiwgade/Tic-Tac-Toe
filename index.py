import itertools

def display_game(game_grid):
    st = " "
    for i in range(len(game_grid)):
        st = st + "  " + str(i)
        
    print(st)
    for count, row in enumerate(game_grid):
        print(count, row)
        

def game_moves(game_grid, player=0, row=0, column=0):
    try:
        if player != 0:
            game_grid[row][column] = player
        return game_grid
    except Exception as e:
        print(str(E))
        return game_grid


def check_winner(check_list):
    if check_list.count(check_list[0]) == len(check_list) and check_list[0] != 0:
        print("Congratulations, The winner is: ", check_list[0])
        return True


def identify_Winner(game_grid):
    try:
        #horizontal winner
        for row in game_grid:
            if check_winner(row):
                return True
        
        #vertical winner
        for cols in range(len(game_grid)):
            vertical=[]
            for row in game_grid:
                vertical.append(row[cols])
            if check_winner(vertical):
                return True
        
        # forward diagnoal winner
        forward_diag = []
        for index in range(len(game_grid)):
            forward_diag.append(game_grid[index][index])
        if check_winner(forward_diag):
            return True
        
        #backward diagonal winner
        backward_diag = []
        for row, col in enumerate(reversed(range(len(game_grid)))):
            backward_diag.append(game_grid[row][col])
        if check_winner(backward_diag):
            return True
    
    except Exception as e:
        print(str(e))
        return False


grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
got_a_winner = False
players = itertools.cycle([1, 2])

while not got_a_winner:
    display_game(grid)
    
    current_player = next(players)
    
    print("Player", current_player, "Make your move, its your turn..")
    row = int(input("Enter the row (0, 1 or 2)"))
    column = int(input("Enter the column (0, 1 or 2)"))
    
    grid = game_moves(grid, current_player, row, column)
    got_a_winner = identify_Winner(grid)
