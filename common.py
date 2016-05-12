import connectfour
import collections

Move = collections.namedtuple('Move', ['Action', 'Col_Num'])

original_gamestate = connectfour.new_game()
game_state = connectfour.GameState
num = [1,2,3,4,5,6,7]


def board_display (gs: connectfour.GameState) -> None:
       '''
       Displays the board from the parameter GameState
       '''
       board = gs.board
       for pick in num:
              print(pick, end = '  ')
       print()
       for row in range(connectfour.BOARD_ROWS):
              for col in range(connectfour.BOARD_COLUMNS):
                     if board[col][row] == connectfour.NONE:
                            print('.', end = '  ')
                     if board[col][row] == connectfour.RED:
                            print('R', end = '  ')
                     if board[col][row] == connectfour.YELLOW:
                            print('Y', end = '  ')
              print()


def display_turn(gs: connectfour.GameState) -> str:
       '''Displays who's turn it is to play'''
       if gs.turn == connectfour.RED:
              print("Red's Turn")
       elif gs.turn == connectfour.YELLOW:
              print("Yellow's Turn")

def interpret_user_input() -> Move:
       '''Take user input on which action the user wants to take and return a
       Move object with the action reflecting a drop or pop move and the column
       number to play in'''
       action_input = input('Please type either D to Drop a piece or P to Pop a piece:')
       if action_input == 'D' or action_input == 'd':
              temp_action = 'D'
              user_column_input= int(input('Please type the column number for the move:'))
              col_num = user_column_input - 1
              if col_num > 0 and col_num < 8:
                     temp_move = Move(temp_action, col_num)
                     return (temp_move)
              else:
                     print('Invalid Column Choice. Try Again')
                     return interpret_user_input()

              
       elif action_input == 'P' or action_input == 'p':
              temp_action = 'P'
              user_column_input= int(input('Please type the column number for the move:'))
              col_num = user_column_input - 1
              if col_num > 0 and col_num < 8:
                     temp_move = Move(temp_action, col_num)
                     return (temp_move)
              else:
                     print('Invalid Column Choice. Try Again')
                     return interpret_user_input()
       else:
              print('Try Again. Please type D or P')
              return interpret_user_input()
              
def user_connection_input() -> tuple:
       '''Takes user input and creates a two-element Python tuple with the first
       element of the tuple being a string identifying the host and the second
       element of the tuple being an integer specifying the port number
       '''
       try:
              host_input = input('Please input a host for the server you wish to connect to, either an IP address or a name:')
              port_input = int(input('Please input a port number for your connection (port number must be an integer in range 0-65535:'))
              return (host_input, port_input)
       except:
              print('Invalid Input: Try Again')
              return user_connection_input()
       

def get_username() -> str:
       '''Takes user input and returns a str representing the username'''
       user_name = input('Please enter a username (Username cannot contain any whitespace -- spaces or tabs --):')
       stripped = user_name.strip()
       for letter in stripped:
              if ' ' in stripped or '\t' in stripped:
                     print('Invalid Username: Try Again')
                     return get_username()
              else:
                     continue

       return stripped
       
                     



       
              
       

              
       








