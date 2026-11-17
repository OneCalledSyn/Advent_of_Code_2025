# with open("C:/Users/jshap/OneDrive/Desktop/aoc3a_input.txt", "r") as f:
#     total = 0

#     for line in f:
#         line = line.strip()
#         L = len(line)
#         first, second = 0,0
#         p1, p2 = 0, L - 1
        
#         for digit in range(L - 1):
#             current = int(line[digit])
#             if current > first:
#                 first = current
#                 p1 = digit
        
#         for digit in range(p1 + 1, L):
#             current = int(line[digit])
#             if current > second:
#                 second = current

#         total += (10*first + second)
    
#     print(total)

with open("C:/Users/jshap/OneDrive/Desktop/aoc3a_input.txt", "r") as f:
    total = 0

    for line in f:
        line = line.strip()
        L = len(line)
        drop = L - 12
        stack = []

        for char in line:
            current = int(char)
            while stack and drop and stack[-1] < current:
                stack.pop()
                drop -= 1
            stack.append(current)

        selected = stack[0:12]
        joltage = 0
        for digit in selected:
            joltage = joltage*10 + digit
        
        total += joltage
    
    print(total)