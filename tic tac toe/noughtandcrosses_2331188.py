import random #generate random number
import os.path #used for file handeling #such as for merging, normalizing and retrieving path names in python . 
import json #helps in editing and modifying . connect  textfile and noughtcross file together 

random.seed() #genrate random data encoding and decoding


def draw_board(board):
    # develop code to draw the board
    #list vitra ko list lai denote gareko
    #row and column 
    print("----------------")
    print(" | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | ")
    print("----------------")
    print(" | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | ")
    print("----------------")
    print(" | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | ")
    print("----------------")
    pass


def welcome(board):
    # prints the welcome message
    # display the board by calling draw_board(board)
    print('Welcome eo the "Unbeatable Nought and Crosses" game.')
    print("The board layout is shown below:")
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want.")
    pass


def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    for i in board: #suru ko linnxa value
        j = 0  # list vitra ko list lai chalauna
        while j < 3: #list vitra ko list lai access garna
            i[j] = ' ' #tyo number haru lai khali sanga replace garxa
            j = j + 1
    return board


def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    choice = int(input("Choose your square:"))
    if choice >= 1 and choice <= 9: #determines position
            if choice == 1 or choice == 2 or choice == 3:
                row = 1
            elif choice == 4 or choice == 5 or choice == 6:
                row = 2
            elif choice == 7 or choice == 8 or choice == 9:
                row = 3
            if choice == 1 or choice == 4 or choice == 7:
                col = 1
            elif choice == 2 or choice == 5 or choice == 8:
                col = 2
            elif choice == 3 or choice == 6 or choice == 9:
                col = 3
           
    else:
            choice = int(input("OUT OF THE BOX. Choose again:"))
    return row, col


def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    choice = random.randrange(1, 10)
    if choice == 1 or choice == 2 or choice == 3:
        row = 1
    elif choice == 4 or choice == 5 or choice == 6:
        row = 2
    elif choice == 7 or choice == 8 or choice == 9:
        row = 3
    if choice == 1 or choice == 4 or choice == 7:
        col = 1
    elif choice == 2 or choice == 5 or choice == 8:
        col = 2
    elif choice == 3 or choice == 6 or choice == 9:
        col = 3
    return row, col #use for calling lateron


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] == mark:
        result = True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] == mark:
        result = True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] == mark:
        result = True
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] == mark:
        result = True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] == mark:
        result = True
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] == mark:
        result = True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] == mark:
        result = True
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] == mark:
        result = True
    else:
        result = False
    return result


def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # repeat the loop
    board = initialise_board(board) #board pass gareko 
    draw_board(board)
    score = 0
    while True:
        row, col = get_player_move(board)
        while True:
            if board[row - 1][col - 1] == ' ':
                board[row - 1][col - 1] = 'X'
                break
            else:
                print("Input already exist.")
                row, col = get_player_move(board)
        draw_board(board)
        if check_for_win(board, 'X') == True:
            return score + 1
        elif check_for_draw(board) == True:
            score = score
            return score
        row, col = choose_computer_move(board)
        while True:
            if board[row - 1][col - 1] == ' ':
                board[row - 1][col - 1] = 'O'
                break
            else:
                row, col = choose_computer_move(board)
        draw_board(board)
        if check_for_win(board, 'O') == True:
            return score - 1
        elif check_for_draw(board) == True:
            return score


def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    print("Enter one of the following options:")
    print("1 - Play the game")
    print("2 - Save score in file 'leaderboard.txt'")
    print("3 - Load and display the scores from the 'leaderboard.txt'")
    print("q - End the program")
    choice = input("1,2,3 or q?? Enter your choice.")
    return choice


def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    if os.path.getsize('leaderboard.txt') != 0:
        file = open("leaderboard.txt", "r")
        read = file.read()
        leaders = json.loads(read) #converts into python code 
        file.close()
    else:
        leaders = {"Leader Board is": "empty"}


def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    user_name = input("Enter User Name : ")
    if os.path.getsize('leaderboard.txt') != 0: #chck empty or full
        file = open("leaderboard.txt", "r+") #r+ read and write
        read = file.read()
        dict_file = json.loads(read) #converts into  python dictionary
        file.seek(0) # add  and read details from the first
        file.truncate() # fix the file size 
        new_dict = {user_name: score}
        final_dict = {**dict_file, **new_dict} #*merged both dictionary takes only key and value
        file.write(json.dumps(final_dict)) #send result to leadrboard and dump le chai leaderboard ko dict ma convet garxa
        file.close()
    else:
        file = open("leaderboard.txt", "w")
        new_dict = {user_name: score}
        file.write(json.dumps(new_dict))
        file.close()


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    print(leaders)
