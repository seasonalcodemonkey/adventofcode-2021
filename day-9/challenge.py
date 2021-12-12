def load_input(filename):
    try:
        file = open(filename, "r")
    except Exception as exc:
        return exc
    
    lines = []

    for line in file:
        lines.append(line.strip())

    file.close()    

    return lines

def parse_input(lines):
    len_x = len(lines[0])
    len_y = len(lines)

    heatmap = [[None for i in range(len_y)] for j in range(len_x)]

    for x in range(len_x):
        for y in range(len_y):
            heatmap[x][y] = int(lines[y][x])
    
    return heatmap

class Grid:
    def __init__(self, grid, len_x, len_y):
        self.len_x = len_x
        self.len_y = len_y

        self.min_x, self.min_y  = 0, 0
        self.max_y = self.len_y - 1
        self.max_x = self.len_x - 1

        self.grid = grid

        self.precompute_corners()
        
    def precompute_corners(self):
         self.corners = {
        (0, 0): [(1, 0), (0, 1)], #top_left 
        (self.max_x, 0): [(self.max_x - 1, 0), (self.max_x, 1)], #top_right 
        (0, self.max_y): [(1, self.max_y), (0, self.max_y - 1)] , #bottom_left
        (self.max_x, self.max_y): [(self.max_x - 1, self.max_y), (self.max_x, self.max_y - 1)] #bottom_right
        }
    
    def adjacent(self, x, y):
        #Corners
        if (x, y) in self.corners:
            return self.corners[(x, y)]
        
        if y == 0: #Top Line
            return [(x - 1, y), (x + 1, y), (x, y + 1)]

        if y == self.max_y: #Bottom Line
            return [(x - 1, y), (x + 1, y), (x, y - 1)]

        if x == 0: #Left Line
            return [(x, y - 1), (x, y + 1), (x + 1, y)]
        
        if x == self.max_x: #Right Line
            return [(x, y - 1), (x, y + 1), (x - 1, y)]

        #Centre
        return [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]

    def find_adjacent(self, x, y, criterion, ignore = []):
        adjacents = self.adjacent(x, y)
        matches = []

        for a_x, a_y in adjacents:
            if criterion(self.grid[x][y], self.grid[a_x][a_y]):
                if (a_x, a_y) not in ignore:
                    matches.append((a_x, a_y))
        
        return matches

    def find_lows(self):
        lows = []
        criterion = lambda o, a: o < a

        for x in range(self.len_x):
            for y in range(self.len_y):
                adjacents = self.adjacent(x, y)
                low = True

                for a_x, a_y in adjacents:
                    if not criterion(self.grid[x][y], self.grid[a_x][a_y]):
                        low = False

                if low:
                    lows.append([self.grid[x][y], (x, y)])
        return lows

    def find_basin(self, low):
        x, y = low
        adjacents = []
        criterion = lambda o, a: a < 9

        adjacents = self.find_adjacent(x, y, criterion)

        for x, y in adjacents:
            adjs = self.find_adjacent(x, y, criterion, adjacents)

            for adj in adjs:
                adjacents.append(adj) 

        return adjacents 

    def find_basins(self, lows):
        basins = []

        for low in lows:
            basin = self.find_basin(low[1])
            basins.append([low[1], len(basin), basin])

        return basins

def risk_level(low_points):
    sum = 0

    for low in [i[0] for i in low_points]:
        sum += low + 1

    return sum

def product_three_largest(basins):
    sizes = [i[1] for i in basins]
    sizes.sort(reverse=True)

    return sizes[0] * sizes[1] * sizes[2]

if __name__ == "__main__":
    filename = "input"
    input = load_input(filename)
    
    if isinstance(input, Exception):
        print("Could not load from %s: %s" % (filename, input)) 
    else:
        heightmap = parse_input(input)
        heightmap = Grid(heightmap, len(heightmap), len(heightmap[0]))
        
        lows = heightmap.find_lows()
        print("Risk level score: %i " % risk_level(lows))
        
        basins = heightmap.find_basins(lows)
        print("Product of three largest: %i" % product_three_largest(basins)) 

