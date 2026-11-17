# def solve_vertical_worksheet(path):
#     with open(path, "r") as f:
#         lines = [ln.rstrip("\n") for ln in f.readlines()]

#     if not lines:
#         return 0

#     # Pad lines to same length
#     width = max(len(ln) for ln in lines)
#     lines = [ln.ljust(width) for ln in lines]

#     rows = len(lines)
#     last_row_index = rows - 1

#     # A column is a separator iff every row has a space there
#     sep_cols = [all(lines[r][c] == " " for r in range(rows)) for c in range(width)]

#     # Build blocks: contiguous runs of columns that are NOT separators
#     blocks = []
#     c = 0
#     while c < width:
#         # skip separator columns
#         if sep_cols[c]:
#             c += 1
#             continue
#         start = c
#         while c < width and not sep_cols[c]:
#             c += 1
#         end = c - 1
#         blocks.append((start, end))

#     grand_total = 0
#     problems = []
#     for start, end in blocks:
#         # collect operands from all rows except the last row
#         operands = []
#         for r in range(0, last_row_index):
#             token = lines[r][start:end+1].strip()
#             if token != "":
#                 # try convert to int (strip possible extra spaces)
#                 try:
#                     operands.append(int(token))
#                 except ValueError:
#                     raise ValueError(f"Expected integer in block {start}-{end} on row {r}: '{token}'")
#         # operator taken from the last row of the block
#         op_token = lines[last_row_index][start:end+1].strip()
#         if not op_token:
#             raise ValueError(f"No operator found in block {start}-{end} on last row.")
#         op = op_token[0]   # expect '+' or '*'

#         if op == "+":
#             result = sum(operands)
#         elif op == "*":
#             result = 1
#             for v in operands:
#                 result *= v
#         else:
#             raise ValueError(f"Unknown operator '{op}' in block {start}-{end}.")

#         problems.append((operands, op, result))
#         grand_total += result

#     # optional: return detailed problem list and grand total
#     return grand_total, problems

from math import prod
lines = open(0).readlines()
total, column, numbers = 0, len(lines[0]) - 2, []
while column >= 0:
    while True:
        numbers.append(int(''.join([line[column] for line in lines[:-1]])))
        if lines[-1][column] == ' ': column -= 1
        else:
            total, numbers, column = total + (sum(numbers) if lines[-1][column] == '+' else prod(numbers)), [], column - 2
            break
print(total)