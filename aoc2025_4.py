# with open("C:/Users/jshap/OneDrive/Desktop/aoc4a_input.txt", "r") as f:
#     lines = [line.rstrip("\n") for line in f]

# warehouse = [list(line) for line in lines]
# directions = [
#         (-1, -1), (-1, 0), (-1, 1),
#         ( 0, -1),          ( 0, 1),
#         ( 1, -1), ( 1, 0), ( 1, 1)
# ]


# rows = len(lines)
# cols = len(lines[0])
# accessible = 0

# for row in range(rows):
#     for col in range(cols):
#         if warehouse[row][col] == "@":
#             neighbors = 0
#             for d_row, d_col in directions:
#                 new_row, new_col = row + d_row, col + d_col
#                 if 0 <= new_row <rows and 0 <= new_col < cols:
#                     if warehouse[new_row][new_col] == "@":
#                         neighbors += 1
#             if neighbors < 4:
#                 accessible += 1

# print(accessible)                        

with open("C:/Users/jshap/OneDrive/Desktop/aoc4a_input.txt", "r") as f:
    lines = [line.rstrip("\n") for line in f]

warehouse = [list(line) for line in lines]
directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
]


rows = len(lines)
cols = len(lines[0])
accessible = 0
delta = 1

while delta > 0:
    delta = 0
    for row in range(rows):
        for col in range(cols):
            if warehouse[row][col] == "@":
                neighbors = 0
                for d_row, d_col in directions:
                    new_row, new_col = row + d_row, col + d_col
                    if 0 <= new_row <rows and 0 <= new_col < cols:
                        if warehouse[new_row][new_col] == "@":
                            neighbors += 1
                if neighbors < 4:
                    accessible += 1
                    delta += 1
                    warehouse[row][col] = "."

print(accessible)