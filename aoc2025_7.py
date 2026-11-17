# with open("C:/Users/jshap/OneDrive/Desktop/aoc7a_input.txt", "r") as f:
#     lines = [list(line.rstrip("\n")) for line in f]

# splits = 0
# width = len(lines[0])
# height = len(lines)

# for i in range(width):
#     if lines[0][i] == "S":
#         lines[1][i] = "|"

# for j in range(1, height-1):
#     for i in range(width):

#         if lines[j][i] == "|" and lines[j+1][i] == ".":
#             lines[j+1][i] = "|"

#         if lines[j][i] == "^" and lines[j-1][i] == "|":
#             splits += 1

#             if i - 1 >= 0 and lines[j+1][i-1] == ".":
#                 lines[j+1][i-1] = "|"

#             if i + 1 < width and lines[j+1][i+1] == ".":
#                 lines[j+1][i+1] = "|"

# print(splits)

with open("C:/Users/jshap/OneDrive/Desktop/aoc7a_input.txt", "r") as f:
    lines = [list(line.rstrip("\n")) for line in f]

width = len(lines[0])
height = len(lines)

# counts[r][c] = number of timelines reaching (r, c)
counts = [[0] * width for _ in range(height)]

# Seed starting beams under every S
for i in range(width):
    if lines[0][i] == "S":
        counts[1][i] = 1

# Process all rows top-down
for r in range(1, height - 1):
    for c in range(width):

        n = counts[r][c]
        if n == 0:
            continue  # no timelines here, skip

        below = lines[r+1][c]

        # 1. Straight fall if empty
        if below == ".":
            counts[r+1][c] += n

        # 2. Split if splitter
        elif below == "^":
            # left branch
            if c - 1 >= 0:
                counts[r+2][c-1] += n
            else:
                # off-grid counts as completed timelines
                pass

            # right branch
            if c + 1 < width:
                counts[r+2][c+1] += n
            else:
                pass

        # 3. Any other char ends timelines (none in your input)
        else:
            pass

# Total timelines = sum of all timelines that ever exited or ended
# Since we never explicitly count "falling out of grid", all timelines
# end somewhere inside the grid. Summing the last row is sufficient.
answer = sum(counts[height-1])

print(answer)