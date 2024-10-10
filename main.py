import random, time

choices = ('Rock', 'Paper', "Scissor")

player_wins = 0
player_losses = 0
player_draws = 0
pc_wins = 0
pc_losses = 0
pc_draws = 0
def show_scores():
    print(f"""
SCOREBOARD  SCOREBOARD  SCOREBOARD  SCOREBOARD  SCOREBOARD  SCOREBOARD  SCOREBOARD 
____________________________________________________________________________________

Player = |||Wins({player_wins})|||Losses({player_losses})|||Draws({player_draws})|||          
NPC    = |||Wins({pc_wins})|||Losses({pc_losses})|||Draws({pc_draws})|||          
____________________________________________________________________________________      
          """)
    print("""
        Menu
--------------------        
1. Return to Menu
2. Start a new Game
3. Quit
""")
    userInput = int(input())
    if userInput == 1:
        menu() 
    if userInput == 2:
        start()
    if userInput == 3:
        exit()

def menu():
    print("""
Welcome to Rock Paper Scissors.          
        Main Menu
-------------------------------       
1. Start Game
2. Check Scores
3. Quit           
-------------------------------          
          """)
    userChoice = int(input())    
    if userChoice == 1:
        print("Starting Game...")
        time.sleep(1)
        start()
    if userChoice == 2:
        show_scores()
    if userChoice == 3:
        exit()
def start():
    global   player_wins, player_losses, player_draws, pc_wins, pc_losses, pc_draws
    player = ""
    games = 3
    while games > 0:
        if games == 0:
            break
        games -= 1
        try:
            player_selection = (input(f"Choose one {choices}:")).lower()
            if player_selection in 'rock':
                player = choices[0].lower()
            elif player_selection in 'paper':
                player = choices[1].lower()
            elif player_selection in 'scissor':
                player = choices[2].lower()
        except:
            print(f"{choices} is an incorrect choice")
        print("you chose "+ player)
        pc_choice = str(random.choices(choices)).replace("['","").replace("']","").lower()
        print("pc chose "+ pc_choice)


        print(f"amount of rounds left {games} ")
        if player in 'rock' and pc_choice in 'rock':
            print('draw')
            player_draws += 1
            pc_draws += 1
        elif player in "rock" and pc_choice in "scissor":
            print("you win")
            player_wins += 1 
            pc_losses += 1
        elif player in "rock" and pc_choice in "paper":
            print("you lose")
            player_losses += 1
            pc_wins += 1
        elif player in 'paper' and pc_choice in 'rock':
            print('win')
            player_wins += 1 
            pc_losses += 1
        elif player in "paper" and pc_choice in "scissor":
            print("you lose")
            player_losses += 1
            pc_wins += 1
        elif player in "paper" and pc_choice in "paper":
            print("you draw")
            player_draws+= 1
            pc_draws += 1
        elif player in 'scissor' and pc_choice in 'rock':
            print('lose')
            player_losses += 1
            pc_wins += 1
        elif player in "scissor" and pc_choice in "scissor":
            print("you draw")
            player_draws+= 1
            pc_draws += 1
        elif player in "scissor" and pc_choice in "paper":
            print("you win")
            player_wins += 1 
            pc_losses += 1
    print("Returning to the Main Menu")
    time.sleep(1)    
    menu()
    
        
menu()
