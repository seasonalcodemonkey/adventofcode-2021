def load_input(filename):
    try:
        file = open(filename, "r")
    except Exception as exc:
        return exc
    
    lines = []

    for line in file:
        lines.append(line)

    file.close()    

    return lines

def calculate_position(commands):    
    horizontal = 0
    depth = 0 

    for command in commands:
        part = command.split(" ")
        
        if len(part) == 2:
            if part[0] == "forward":
                horizontal += int(part[1])
            elif part[0] == "up":
                depth -= int(part[1])
            elif part[0] == "down":
                depth += int(part[1])

    return (horizontal, depth)

def calculate_position_aim(commands):    
    horizontal = 0
    depth = 0 
    aim = 0

    for command in commands:
        part = command.split(" ")
        
        if len(part) == 2:
            if part[0] == "forward":
                horizontal += int(part[1])
                depth += aim * int(part[1])
            elif part[0] == "up":
                aim -= int(part[1])
            elif part[0] == "down":
                aim += int(part[1])

    return (horizontal, depth)

if __name__ == "__main__":
    filename = "input"
    commands = load_input(filename)

    position = calculate_position(commands)
    print("%s multiplied is %i" % (position, position[0] * position[1]))

    position = calculate_position_aim(commands)
    print("%s multiplied is %i" % (position, position[0] * position[1]))

