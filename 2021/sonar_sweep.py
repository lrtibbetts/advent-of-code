
measurements = []

with open('sonar_input.txt') as f:
    for line in f:
        measurements.append(int(line.strip()))

print(len(measurements))

ptr_1 = 0
ptr_2 = 1
num_increases = 0

while ptr_2 + 2 < len(measurements):
    first_sum = measurements[ptr_1] + measurements[ptr_1+1] + measurements[ptr_1+2]
    second_sum = measurements[ptr_2] + measurements[ptr_2+1] + measurements[ptr_2+2]

    if second_sum > first_sum:
        num_increases += 1
    
    ptr_1 += 1
    ptr_2 += 1

print(num_increases)