import curses

# Keybinds

# Board/Map Class
class board:
    def __init__(self, width= 120, height = 20, char="█"):
        self.height = height
        self.width = width
        self.char = char
        self.board = self.generate_board(char, width, height)


    def generate_board(self, char, width, height):
        board = []
        tb = char*width # Used to generate the top and bottom of the board
        mid = char + (" "*(width-2)) + char # Used to generate the sections in between the top and bottom
        board.append(tb) # Create topmost line
        for i in range(height): # Create middle of map
            board.append(mid)
        board.append(tb) # Create Bottommost line
        return board
    
    def __radd__(self, other):
        pass

# Snake class
class snake:
    def __init__(self):
        pass

    def __add__(self, other):
        pass
    
    def __radd__(self, other):
        pass


# Food
class food:
    def __init__(self):
        pass

    def __add__(self, other):
        pass
    
    def __radd__(self, other):
        pass


# Gameloop



# Testing

if __name__ == "__main__":
    a = board()
    for i in (a.board):
        print(i)