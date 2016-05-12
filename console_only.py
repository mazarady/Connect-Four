import connectfour
import common


def each_turn() -> None:
       '''
       Simulates turn for each player, updates gamestate, displays the
       board for the user to see and shows whose turn it is. Breaks and
       Displays the winner when the game is won.
       
       '''
       game = connectfour.new_game()


       while True:
              common.display_turn(game)
              player_move = common.interpret_user_input()
              
              if player_move.Action == 'D':
                     try:
                            game = connectfour.drop(game, player_move.Col_Num)
                            print()
                            common.board_display(game)
                     except:
                            print('Invalid Move')
              
                            
              elif player_move.Action == 'P':
                     try:
                            game = connectfour.pop(game, player_move.Col_Num)
                            print()
                            common.board_display(game)
                     except:
                            print('Invalid Move')
                            
              else:
                     print('Try again')
                     
              if winner(game):
                     break

def winner(game) -> bool:
       if connectfour.winner(game) == connectfour.RED:
              print('Red is the winner')
              return True
       
       elif connectfour.winner(game) == connectfour.YELLOW:
              print("Yellow is the winner")
              return True
       else:
              return False       

def play_connectfour():
       '''
       Starts the game of connect four and allows users to play
       '''
       print("Welcome To Connect Four")
       common.board_display(common.original_gamestate)            
       each_turn()
       
if __name__ == '__main__':
       play_connectfour()
