import random

# Defines the snakes and ladders separately

# This dictionary represents the positions on the board where players will encounter snakes.
snakes = { 
    17: 4, 
    19: 7, 
    27: 1, 
    24: 16 
}


# This dictionary represents the positions on the board where players will encounter ladders.
ladders = { 
    3: 22, 
    5: 8, 
    11: 26, 
    20: 29 
}

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, steps):
        self.position += steps
        if self.position > 30:  # Assuming 30 is the last square
            self.position = 30
        
        # Check for snakes or ladders
        if self.position in ladders:
            self.position = ladders[self.position]
            print(f"{self.name} climbed a ladder to {self.position}")
        elif self.position in snakes:
            self.position = snakes[self.position]
            print(f"{self.name} slid down a snake to {self.position}")

        print(f"{self.name} moved to {self.position}")

def roll_dice():
    return random.randint(1, 6)

def play_game(players):
    while True:
        for player in players:
            input(f"{player.name}'s turn. Press Enter to roll the dice...")
            dice_value = roll_dice()
            print(f"{player.name} rolled a {dice_value}")
            player.move(dice_value)

            # Check for win condition
            if player.position == 30:
                print(f"{player.name} wins!")
                return

def main():
    num_players = int(input("Enter number of players: "))
    players = []
    
    for i in range(num_players):
        name = input(f"Enter name for player {i + 1}: ")
        players.append(Player(name))
    
    play_game(players)

if __name__ == "__main__":
    main()
