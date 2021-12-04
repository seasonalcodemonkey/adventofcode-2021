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

def power_consumption(input):
    line, line_i = [], 0 
    line_len, line_count = len(input[0]), len(input)
    count = [0 for i in range(0, line_len)]
    gamma, epsilon = 0, 0
    
    for i in input:
        line.append(int(i, 2))

    while line_i < line_count:
        for i in range(0, line_len): 
            bitpos = line_len - i - 1
            count[i] += (line[line_i] & (2**bitpos)) >> bitpos

        line_i = line_i + 1

    for i in range(0, line_len):
        threshold = (line_count - (line_count % 2)) // 2
        
        if count[i] > threshold:
            bitpos = line_len - i - 1
            gamma +=  2**bitpos

    epsilon = gamma ^ ((2**line_len) - 1)

    return (gamma, epsilon)

if __name__ == "__main__":
    filename = "input"
    input = load_input(filename)
    
    if isinstance(input, Exception):
        print("Could not load from %s: %s" % (filename, input)) 
    else:
        result = power_consumption(input)
        print("Epsilon: %i Gamma: %i product: %i" % (result[1], result[0], result[0] * result[1]))