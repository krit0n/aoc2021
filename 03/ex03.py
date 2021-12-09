def bits_complement(bits):
    return [abs(b - 1) for b in bits]

def _powers(n):
    v = 1
    while True:
        yield v
        v *= n

def bits_to_int(bits):
    return sum(bit * base for bit, base in zip(reversed(bits),_powers(2)))


with open('input.txt') as file:
    lines = (line.strip() for line in file)
    bits = [list(map(int, list(line))) for line in lines]

## exercise 1

gammarate_bits = [int(sum(i)*2 > len(i)) for i in zip(*bits)]
epsilonrate_bits = bits_complement(gammarate_bits)
gammarate = bits_to_int(gammarate_bits)
epsilonrate = bits_to_int(epsilonrate_bits)

print("solution 1:", gammarate, "*", epsilonrate, "=", gammarate * epsilonrate)



## exercise 2

def get_oxygen_rating(bits, index = 0):
    if 1 == len(bits):
        return bits[0]
    else:
        msbs = [bs[index] for bs in bits]
        most_common_first_bit = int(sum(msbs)*2 >= len(msbs))
        return get_oxygen_rating([bs for bs in bits if bs[index] == most_common_first_bit], index + 1)

def get_scrubber_rating(bits, index = 0):
    if 1 == len(bits):
        return bits[0]
    else:
        msbs = [bs[index] for bs in bits]
        most_common_first_bit = int(sum(msbs)*2 < len(msbs))
        return get_scrubber_rating([bs for bs in bits if bs[index] == most_common_first_bit], index + 1)

oxrating = bits_to_int(get_oxygen_rating(bits))
scrating = bits_to_int(get_scrubber_rating(bits))
print("solution 2:", oxrating, "*", scrating, "=", oxrating * scrating)
