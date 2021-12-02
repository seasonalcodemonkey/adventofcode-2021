def load_input(filename):
    try:
        file = open(filename, "r")
    except Exception as exc:
        return exc
    
    lines = []

    for line in file:
        lines.append(int(line))

    file.close()    

    return lines
    
def depth_increases(depth):
    increases_count = 0

    for i in range(0, len(depth) - 1):
        if depth[i+1] > depth[i]:
            increases_count += 1

    return increases_count

def sliding_window(depth):
    window_size = 3
    window = []
    sum = 0

    len_depth = len(depth)
    last_full_window = len_depth - 2
    
    for i in range(0, last_full_window):
        for j in range(0, window_size):
            sum += depth[i + j]
        
        window.append(sum)
        sum = 0

    return depth_increases(window)

if __name__ == "__main__":
    filename = "input"
    depths = load_input(filename)

    if isinstance(depths, Exception):
        print("Could not load from %s: %s" % (filename, depths)) 
    else:
        print("Total increases: %i" % depth_increases(depths))
        print("Total window increases %i" % sliding_window(depths))
    


