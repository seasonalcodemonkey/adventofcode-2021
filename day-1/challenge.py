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

if __name__ == "__main__":
    filename = "input"
    depths = load_input(filename)

    if isinstance(depths, Exception):
        print("Could not load from %s: %s" % (filename, depths)) 
    else:
        print("Total increases: %i" % depth_increases(depths))


