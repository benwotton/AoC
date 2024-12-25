"""AoC 2024 | Day 1 | Part 2"""
from collections import Counter

left_list, right_list = [], []
with open("input.txt", "r") as file:
    for line in file:
        val1, val2 = map(int, line.split())
        left_list.append(val1)
        right_list.append(val2)

counter = Counter(right_list)
similarity_score = 0
for value in left_list:
    similarity_score += value * counter[value]

print(similarity_score)
