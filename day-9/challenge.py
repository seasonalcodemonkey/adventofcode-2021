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

def low_points(heatmap):
    len_x = len(heatmap)
    len_y = len(heatmap[0])
    lows = []

    add_low = lambda x, y: lows.append([heatmap[x][y], (x+1,y+1)])

    #Corners
    top_left = [(0, 0), [(1, 0), (0, 1)]]
    top_right = [(len_x - 1, 0), [(len_x - 2, 0), (len_x - 1, 1)]]
    bottom_left = [(0, len_y - 1), [(1, len_y - 1), (0, len_y - 2)]]
    bottom_right = [(len_x - 1, len_y - 1), [(len_x - 2, len_y - 1), (len_x - 1, len_y - 2)]]
    corners = [top_left, top_right, bottom_left, bottom_right]

    xy, neighbour = 0, 1

    for corner in corners:
        x, y = corner[xy]
        low = True

        for n_x, n_y in corner[neighbour]:
            if not heatmap[x][y] < heatmap[n_x][n_y]:
                low = False
                break
        
        if low:
            add_low(x, y)

    #Top line
    y = 0
    for x in range(1, len_x - 1):
        low = True

        for n_x, n_y in [(x - 1, y), (x + 1, y), (x, y + 1)]:
            if not heatmap[x][y] < heatmap[n_x][n_y]:
                low = False
                break
        
        if low:
            add_low(x, y)

    #Bottom line
    y = len_y - 1
    for x in range(1, len_x - 1):
        low = True

        for n_x, n_y in [(x - 1, y), (x + 1, y), (x, y - 1)]:
            if not heatmap[x][y] < heatmap[n_x][n_y]:
                low = False
                break
        
        if low:
            add_low(x, y)

    #Left line
    x = 0
    for y in range(1, len_y - 1):
        low = True

        for n_x, n_y in [(x, y - 1), (x, y + 1), (x + 1, y)]:
            if not heatmap[x][y] < heatmap[n_x][n_y]:
                low = False
                break
        
        if low:
            add_low(x, y)

    #Right line
    x = len_x - 1
    for y in range(1, len_y - 1):
        low = True

        for n_x, n_y in [(x, y - 1), (x, y + 1), (x - 1, y)]:
            if not heatmap[x][y] < heatmap[n_x][n_y]:
                low = False
                break
        
        if low:
            add_low(x, y)

    #Centre
    for x in range(1, len_x - 1):
        for y in range(1, len_y - 1):
            low = True

            for n_x, n_y in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
                if not heatmap[x][y] < heatmap[n_x][n_y]:
                    low = False
                    break
            
            if low:
                add_low(x, y)

    return lows

def risk_level(low_points):
    sum = 0

    for low in [i[0] for i in low_points]:
        sum += low + 1

    return sum

if __name__ == "__main__":
    filename = "input"
    input = load_input(filename)
    
    if isinstance(input, Exception):
        print("Could not load from %s: %s" % (filename, input)) 
    else:
        heatmap = parse_input(input)
        lows = low_points(heatmap)
        print("Risk level score: %i " % risk_level(lows))


