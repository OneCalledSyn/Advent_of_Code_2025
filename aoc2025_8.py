# boxes = []

# with open("C:/Users/jshap/OneDrive/Desktop/aoc8a_input.txt", "r") as f:
#     for line in f:
#         boxes.append(line.rstrip("\n").split(","))

# print(boxes)

# Read the input





points = []
with open("C:/Users/jshap/OneDrive/Desktop/aoc8a_input.txt") as f:
    for line in f:
        x, y, z = line.strip().split(",")
        points.append((int(x), int(y), int(z)))

n = len(points)
print(points)

circuits = []
for i in range(n):
    circuits.append(i)

pairs= []
for i in range(n):
    x1, y1, z1 = points[i]
    for j in range(i + 1, n):
        x2, y2, z2 = points[j]
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        dz = abs(z1 - z2)
        distance = dx*dx + dy*dy + dz*dz
        pairs.append((distance, i, j))

pairs.sort()
print(pairs)

connections = 0

for dist, a, b in pairs:
    if connections == 1000:
        break

    circuit_a = None
    circuit_b = None

    for c in circuits:
        if a in c:
            circuit_a = c
        if b in c:
            circuit_b = c

    if circuit_a == circuit_b:
        continue

    circuit_a.extend(circuit_b)
    circuits.remove(circuit_b)
    connections += 1

sizes = []
for c in circuits:
    sizes.append(len(c))

sizes.sort(reverse=True)

answer = sizes[0] * sizes[1] * sizes[2]
print(answer)