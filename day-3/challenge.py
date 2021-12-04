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

def count_bits(input, count_bit = None, index = False):    
    line, line_i = [], 0 
    line_len, line_count = len(input[0]), len(input)
    count_bit = range(0, line_len) if count_bit == None else [count_bit]
    count = [[0, 0, [[], []]] for i in count_bit]

    for i in input:
        line.append(int(i, 2))

    while line_i < line_count:
        count_i = 0

        for i in count_bit: 
            bitpos = line_len - i - 1
            bit = (line[line_i] & (2**bitpos)) >> bitpos

            if bit == 0:
                count[count_i][0] += 1
            else:
                count[count_i][1] += 1

            if index: 
                count[count_i][2][bit].append(line_i)

            count_i = count_i + 1

        line_i = line_i + 1
        

    return count

def power_consumption(input):
    line, line_len, line_count = [], len(input[0]), len(input)
    gamma, epsilon = 0, 0
    
    count = count_bits(input)

    for i in range(0, line_len):
        threshold = (line_count - (line_count % 2)) // 2
        
        if count[i][1] > threshold:
            bitpos = line_len - i - 1
            gamma +=  2**bitpos

    epsilon = gamma ^ ((2**line_len) - 1)

    return (gamma, epsilon)

def life_support(input):
    criteria = {lambda a, b: a > b, lambda a, b: b > a }
    result = []

    for criterion in criteria:
        selection = input
        bit_i = 0

        while len(selection) > 1:
            count = count_bits(selection, bit_i, True)
            
            zero_count, one_count = count[0][0], count[0][1]
            index = count[0][2]
            
            bit = 0 if criterion(zero_count, one_count) else 1
            bit = 1 if zero_count == one_count and criterion(1, 0) else bit
            bit = 0 if zero_count == one_count and criterion(0, 1) else bit

            selection = [selection[i] for i in index[bit]]
            
            bit_i = bit_i + 1
        
        result.append(selection[0])

    oxygen, co2scrub = int(result[0], 2), int(result[1], 2)

    return (oxygen, co2scrub)

    
if __name__ == "__main__":
    filename = "input"
    input = load_input(filename)
    
    if isinstance(input, Exception):
        print("Could not load from %s: %s" % (filename, input)) 
    else:
        result = power_consumption(input)
        print("Epsilon: %i Gamma: %i product: %i" % (result[1], result[0], result[0] * result[1]))
        
        result = life_support(input)
        print("Oxygen: %i CO2Scrub: %i product: %i" % (result[0], result[1], result[0] * result[1]))