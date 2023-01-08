

horiz = 0
depth = 0
aim = 0

with open('dive_input.txt') as f:
    for line in f:
        directions = line.split(' ')
        if (len(directions) != 2):
            print('something went wrong')

        amt = int(directions[1])

        if (directions[0] == 'forward'):
            horiz = horiz + amt
            depth = depth + (aim * amt)
        elif (directions[0] == 'down'):
            aim = aim + amt
        elif (directions[0] == 'up'):
            aim = aim - amt

print(f'horizontal position: {horiz}')
print(f'depth: {depth}')
print(f'product: {horiz * depth}')