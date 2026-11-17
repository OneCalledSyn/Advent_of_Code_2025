# with open("C:/Users/jshap/OneDrive/Desktop/aoc2a_input.txt", "r") as f:
#     content = f.read()
#     print(content)

# total = 0
# ranges = content.split(",")

# for elt in ranges:
#     print(elt)
#     first, last = map(int, elt.split("-"))
#     for num in range(first, last + 1):
#         string = str(num)
#         if len(string) % 2 != 0:
#             continue
#         mid = len(string) // 2
#         if string[mid:] == string[:mid]:
#             total += num

# print(total)

with open("C:/Users/jshap/OneDrive/Desktop/aoc2a_input.txt", "r") as f:
    content = f.read()
    print(content)

total = 0
ranges = content.split(",")

for elt in ranges:
    print(elt)
    first, last = map(int, elt.split("-"))
    for num in range(first, last + 1):
        string = str(num)
        l = len(string)

        for size in range(1, l // 2 + 1):
            if l % size == 0:
                chunk = string[:size]
                if chunk * (l // size) == string:
                    total += num
                    break

print(total)