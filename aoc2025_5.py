# with open("C:/Users/jshap/OneDrive/Desktop/aoc5a_input.txt", "r") as f:
#     halves = f.read().strip().split("\n\n")

# ranges = halves[0].split("\n")
# ids = halves[1].split("\n")

# fresh = 0

# for id in ids:
#     for range in ranges:
#         start, end = range.split("-")
#         if int(start) <= int(id) <= int(end):
#             fresh += 1
#             break

# print(fresh)

with open("C:/Users/jshap/OneDrive/Desktop/aoc5a_input.txt", "r") as f:
    halves = f.read().strip().split("\n\n")

fresh_ids = 0
ranges = halves[0].split("\n")

intervals = []
for range in ranges:
    a, b = range.split("-")
    intervals.append([int(a), int(b)])
intervals.sort()

merged = []
for a, b in intervals:
    if not merged or a > merged[-1][1]:
        merged.append([a, b])
    else:
        merged[-1][1] = max(merged[-1][1], b)

for x, y in merged:
    fresh_ids += int(y) - int(x) + 1

print(fresh_ids)