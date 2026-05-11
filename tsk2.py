class NavalBattle:
    """
    A class representing a Battleship game with a shared playing field for all players.
    
    Class Attributes:
        playing_field (list): A 10x10 game field represented as a list of lists.
    
    Attributes:
        symbol (str): The symbol used to mark hits made by this player.
    """
    
    playing_field = [[0] * 10 for _ in range(10)]
    
    def __init__(self, symbol: str) -> None:
        """
        Initialize a new player with their unique hit marker symbol.
        
        Args:
            symbol (str): The symbol that will mark this player's hits on the field.
        """
        self.symbol = symbol
    
    def shot(self, x: int, y: int) -> bool:
        """
        Make a shot at the specified coordinates.
        
        Args:
            x (int): The x-coordinate (column) starting from 1 (left to right, 1-10).
            y (int): The y-coordinate (row) starting from 1 (top to bottom, 1-10).
        
        Returns:
            bool: True if the shot hit a ship, False if it missed.
        """
        x_index = x - 1
        y_index = y - 1
        
        if not (0 <= x_index < 10 and 0 <= y_index < 10):
            print("Неверные координаты")
            return False
        
        cell = NavalBattle.playing_field[y_index][x_index]
        
        if cell == 1:
            NavalBattle.playing_field[y_index][x_index] = self.symbol
            print("попал")
            return True
        elif cell == 0:
            NavalBattle.playing_field[y_index][x_index] = "o"
            print("мимо")
            return False
        else:
            print("мимо")
            return False
    
    @staticmethod
    def show() -> None:
        print("\n    1  2  3  4  5  6  7  8  9  10")
        print("   " + "-" * 31)
        
        for i in range(10):
            row_display = []
            for j in range(10):
                cell = NavalBattle.playing_field[i][j]
                
                if cell == 0 or cell == 1:
                    row_display.append("~")
                elif cell == "o":
                    row_display.append("o")
                else:
                    row_display.append(cell)
            
            print(f"{i+1:2d} | " + "  ".join(row_display))
        print()
    
    def __str__(self) -> str:
        return f"Player with symbol '{self.symbol}'"


def main() -> None:
    """
    The main function demonstrating the NavalBattle class functionality.
    """
    print("=" * 50)
    print("NAVAL BATTLE GAME")
    print("=" * 50)
    
    NavalBattle.playing_field = [
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 1],  # Row 1
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # Row 2
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # Row 3
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 0],  # Row 4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 5
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 6
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 7
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Row 10
    ]
    
    player1 = NavalBattle("#")
    player2 = NavalBattle("*")
    
    print("Initial playing field (all hidden):")
    NavalBattle.show()
    
    print("Making shots...")
    print("-" * 50)
    
    print("Player 1 (#) shots:")
    player1.shot(6, 2)
    player1.shot(6, 1)
    
    print("\nPlayer 2 (*) shots:")
    player2.shot(6, 3)
    player2.shot(6, 4)
    player2.shot(6, 5)
    player2.shot(3, 3)
    
    print("\nPlayer 1 (#) additional shot:")
    player1.shot(1, 1)
    
    print("\n" + "=" * 50)
    print("Final playing field:")
    NavalBattle.show()
    
    print("Players:")
    print(f"  {player1}")
    print(f"  {player2}")


if __name__ == "__main__":
    main()
