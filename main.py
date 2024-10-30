import random, time
class player():
    def __init__(self, name, wins, losses, draws):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.draws = draws
    def __str__(self):
        return f'{self.name} - {self.wins} wins, {self.losses} losses, {self.draws} draws'
    def add_win(self):
        self.wins += 1
    def add_loss(self):
        self.losses += 1
    def add_draw(self):
        self.draws += 1
    
                    
choices = ('Rock', 'Paper', "Scissor")

pc_wins = 0
pc_losses = 0
pc_draws = 0


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
        #show scores 
        pass
    if userChoice == 3:
        exit()
def start():
    global   player_wins, player_losses, player_draws, pc_wins, pc_losses, pc_draws
    new_player = player(input("Enter your name: "), 0, 0, 0)
    
    games = 3
    while games > 0:
        if games == 0:
            break
        games -= 1
        try:
            player_selection = (input(f"Choose one {choices}:")).lower()
            if player_selection in 'rock':
                action = choices[0].lower()
            elif player_selection in 'paper':
                action = choices[1].lower()
            elif player_selection in 'scissor':
                action = choices[2].lower()
        except:
            print(f"{choices} is an incorrect choice")
        print("you chose "+ action)
        pc_choice = str(random.choices(choices)).replace("['","").replace("']","").lower()
        print("pc chose "+ pc_choice)


        print(f"amount of rounds left {games} ")
        if action == pc_choice:
            print('draw')
            player.add_draw(new_player)
            pc_draws += 1
        elif (action == 'rock' and pc_choice == 'scissor') or (action == 'scissor' and pc_choice == 'paper') or (action == 'paper' and pc_choice == 'rock'):
            print("you win")
            player.add_win(new_player)
            pc_losses += 1
        else:
            print("you lose")
            player.add_loss(new_player)
            pc_wins += 1
 
    menu()
        
menu()
