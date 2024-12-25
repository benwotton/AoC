"""AoC 2024 | Day 1 | Part 1"""

left_list, right_list = [], []
with open("input.txt", "r") as file:
    for line in file:
        val1, val2 = map(int, line.split())
        left_list.append(val1)
        right_list.append(val2)

left_list.sort()
right_list.sort()

total_distance = 0
for i in range(0, len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])

print(total_distance)
