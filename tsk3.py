import random


class NavalBattle:
    """
    A class representing a Battleship game with a shared playing field for all players.
    
    Class Attributes:
        playing_field (list): A 10x10 game field represented as a list of lists.
        field_initialized (bool): Flag indicating whether the playing field has been set up.
    """
    
    playing_field = None
    field_initialized = False
    
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
        if not NavalBattle.field_initialized or NavalBattle.playing_field is None:
            print("игровое поле не заполнено")
            return False
        
        x_index = x - 1
        y_index = y - 1
        
        if not (0 <= x_index < 10 and 0 <= y_index < 10):
            print("Неверные координаты")
            return False
        
        cell = NavalBattle.playing_field[y_index][x_index]
        
        if cell != 0 and cell != 1:
            print("ошибка")
            return False
        
        if cell == 1:
            NavalBattle.playing_field[y_index][x_index] = self.symbol
            print("попал")
            return True
        else:  
            NavalBattle.playing_field[y_index][x_index] = "o"
            print("мимо")
            return False
    
    @staticmethod
    def show() -> None:
        """
        Display the current state of the playing field.
        """
        if not NavalBattle.field_initialized or NavalBattle.playing_field is None:
            print("игровое поле не заполнено")
            return
        
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
            
            print(" ".join(row_display))
        print()
    
    @classmethod
    def new_game(cls) -> None:
        """
        Create a new game field and randomly place ships on it.
        """
        cls.playing_field = [[0 for _ in range(10)] for _ in range(10)]
        
        ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]  
        
        for ship_size in ships:
            placed = False
            attempts = 0
            
            while not placed and attempts < 1000:
                orientation = random.choice([0, 1])
                
                if orientation == 0: 
                    max_x = 10 - ship_size
                    max_y = 10
                else: 
                    max_x = 10
                    max_y = 10 - ship_size
                
                start_x = random.randint(0, max_x - 1)
                start_y = random.randint(0, max_y - 1)
                
                if cls._can_place_ship(start_x, start_y, ship_size, orientation):
                    cls._place_ship(start_x, start_y, ship_size, orientation)
                    placed = True
                
                attempts += 1
            
            if not placed:
                cls.new_game()
                return
        
        cls.field_initialized = True
    
    @classmethod
    def _can_place_ship(cls, x: int, y: int, size: int, orientation: int) -> bool:
        """
        Check if a ship can be placed at the specified position.
        
        Args:
            x (int): Starting x-coordinate (0-based)
            y (int): Starting y-coordinate (0-based)
            size (int): Length of the ship
            orientation (int): 0 - horizontal, 1 - vertical
        
        Returns:
            bool: True if the ship can be placed, False otherwise
        """
        ship_cells = []
        for i in range(size):
            if orientation == 0: 
                nx, ny = x + i, y
            else:
                nx, ny = x, y + i
            
            if nx >= 10 or ny >= 10:
                return False
            ship_cells.append((nx, ny))

        for nx, ny in ship_cells:
            if cls.playing_field[ny][nx] != 0:
                return False
        
        for nx, ny in ship_cells:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    adj_x, adj_y = nx + dx, ny + dy
                    if 0 <= adj_x < 10 and 0 <= adj_y < 10:
                        if cls.playing_field[adj_y][adj_x] != 0:
                            return False
        
        return True
    
    @classmethod
    def _place_ship(cls, x: int, y: int, size: int, orientation: int) -> None:
        """
        Place a ship on the playing field.
        
        Args:
            x (int): Starting x-coordinate (0-based)
            y (int): Starting y-coordinate (0-based)
            size (int): Length of the ship
            orientation (int): 0 - horizontal, 1 - vertical
        
        Returns:
            None
        """
        for i in range(size):
            if orientation == 0:  
                nx, ny = x + i, y
            else:  
                nx, ny = x, y + i
            cls.playing_field[ny][nx] = 1
    
    def __str__(self) -> str:
        """
        Return a string representation of the player.
        
        Returns:
            str: The player's symbol as a string representation.
        """
        return f"Player with symbol '{self.symbol}'"


def main() -> None:
    """
    The main function demonstrating the NavalBattle class functionality.
    """
    print("=" * 50)
    print("NAVAL BATTLE GAME")
    print("=" * 50)
    
    NavalBattle.new_game()
    
    player1 = NavalBattle('#')
    player2 = NavalBattle('*')
    
    print("Initial playing field (all hidden):")
    NavalBattle.show()
    
    print("Player 1 (#) shots:")
    player1.shot(6, 2)  
    player1.shot(6, 2)  
    
    print("\nAfter shots:")
    NavalBattle.show()
    
    print("\nStarting a NEW GAME...")
    NavalBattle.new_game()
    NavalBattle.show()
    
    player1.shot(6, 2)
    NavalBattle.show()


if __name__ == "__main__":
    main()
