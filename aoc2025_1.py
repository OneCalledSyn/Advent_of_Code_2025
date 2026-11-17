# current = 50
# zeroes = 0

# with open("C:/Users/jshap/OneDrive/Desktop/aoc1a_input.txt", "r") as f:
#     for line in f:
#         #print(line.strip())
#         if line[0] == "R":
#             current += int(line[1:])
#         if line[0] == "L":
#             current -= int(line[1:])

        
#         current %= 100

#         if current == 0:
#             zeroes += 1

# print(zeroes)


# current = 50
# zeroes = 0

# with open("C:/Users/jshap/OneDrive/Desktop/aoc1a_input.txt", "r") as f:
#     for line in f:
#         #print(line.strip())
#         if line[0] == "R":
#             current += int(line[1:])
#         if line[0] == "L":
#             current -= int(line[1:])

#         while current > 99 or current < 0:
#             if current < 0:
#                 current += 100
#             else:
#                 current -= 100
#             zeroes += 1

# print(zeroes)

current = 50
zeroes = 0

with open("C:/Users/jshap/OneDrive/Desktop/aoc1a_input.txt", "r") as f:
    for line in f:
        
        direction = line[0]
        turn = int(line[1:])
        step = 1 if direction == "R" else -1

        
        for _ in range(turn):
            current = (current + step) % 100

            if current == 0:
                zeroes += 1

print(zeroes)