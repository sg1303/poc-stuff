"""
Clone of 2048 game.
"""

# import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    merged_list = []
    length = len(line)
    for dummy_index in range(length):
        merged_list.append(0)

    curr = 0
    curr_index = 0
    for index in range(length):
        if line[index] > 0:
            if curr == 0:
                curr = line[index]
            else:
                if curr == line[index]:
                    merged_list[curr_index] = curr + line[index]
                    curr = 0
                else:
                    merged_list[curr_index] = curr
                    curr = line[index]
                    
                curr_index += 1

    if curr != 0:
        merged_list[curr_index] = curr

    return merged_list

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self.reset()
        self.compute_edges()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_index in range(self._width)] for dummy_index in range(self._height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid = ''
        for row in range(self._height):
            for col in range(self._width):
                grid += str(self._grid[row][col]) + ' '
            grid += '\n'
            
        return grid    

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        edge_tiles = self._edges[direction]
        offset = OFFSETS[direction]
        changed = False
        
        for tile in edge_tiles:
            curr_tiles = []
            row, col = tile[0], tile[1]
            
            # Copy all the tiles in the row or col 
            # associated with the direction of movement
            while row >= 0 and row < self._height and col >= 0 and col < self._width:
                curr_tiles.append(self.get_tile(row, col))
                row += offset[0]
                col += offset[1]
            
            # Perform the move/merge using helper method
            new_tiles = merge(curr_tiles)
            
            # Copy the moved/merged tiles back into the grid
            row, col = tile[0], tile[1]
            num_tiles = len(new_tiles)
            for index in range(num_tiles):
                self.set_tile(row, col, new_tiles[index])
                row += offset[0]
                col += offset[1]
            
            # Compare the lists for changes
            if(curr_tiles != new_tiles):
                changed = True
        
        # Add a new tile if any tiles moved
        if changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        random.seed()
        
        rand = random.random()
        if rand < 0.9:
            tile_val = 2
        else:
            tile_val = 4
        
        # Ensure the new tile is created for an empty square only
        y_max = self._height - 1
        x_max = self._width - 1
        row = random.randint(0, y_max)
        col = random.randint(0, x_max)
        while self._grid[row][col] != 0:
            row = random.randint(0, y_max)
            col = random.randint(0, x_max)
            
        self.set_tile(row, col, tile_val)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]
    
    def compute_edges(self):
        """
        Compute the edge tiles associated with each direction of movement.
        """
        edges = {}
        up_edge, down_edge, left_edge, right_edge = [], [], [], []
        
        for index in range(self._width):
            up_edge.append((0, index))
            down_edge.append((self._height - 1, index))
        
        for index in range(self._height):
            left_edge.append((index, 0))
            right_edge.append((index, self._width - 1))    
        
        edges[UP] = up_edge
        edges[DOWN] = down_edge
        edges[LEFT] = left_edge
        edges[RIGHT] = right_edge
        
        self._edges = edges

# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))