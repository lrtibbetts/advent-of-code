
from collections import namedtuple

counts = {}

BitCount = namedtuple('BitCount', ['zero_count', 'one_count'])

with open('diagnostic_input.txt') as f:
    for line in f:
        for index, char in enumerate(line.strip()):
            key = index
            if key not in counts:
                if (int(char) == 0):
                    counts[key] = BitCount(1, 0)
                else:
                    counts[key] = BitCount(0, 1)
            else:
                curr_count = counts[key]
                if (int(char) == 0):
                    counts[key] = BitCount(curr_count.zero_count + 1, curr_count.one_count)
                else:
                    counts[key] = BitCount(curr_count.zero_count, curr_count.one_count + 1)

print(counts)

gamma_bit_str = ''
epsilon_bit_str = ''

for digit in counts:
    if (counts[digit].zero_count > counts[digit].one_count):
        gamma_bit_str = gamma_bit_str + '0'
        epsilon_bit_str = epsilon_bit_str + '1'
    else:
        gamma_bit_str = gamma_bit_str + '1'
        epsilon_bit_str = epsilon_bit_str + '0'

print(gamma_bit_str)
print(epsilon_bit_str)

gamma = int(gamma_bit_str, 2)
print(gamma)

epsilon = int(epsilon_bit_str, 2)
print(epsilon)

pwr = gamma * epsilon
print(f'power is: {pwr}')