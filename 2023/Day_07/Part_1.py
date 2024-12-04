from collections import Counter
import functools


with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_07\input.txt") as file:
    lines = file.read().split('\n')


def hand_level(hand):
    kinds = sorted(Counter(hand).values(), reverse=True)
    if kinds == [5]:
        return 1
    if kinds == [4, 1]:
        return 2
    if kinds == [3, 2]:
        return 3
    if kinds == [3, 1, 1]:
        return 4
    if kinds == [2, 2, 1]:
        return 5
    if kinds == [2, 1, 1, 1]:
        return 6
    return 7


def compare_rank(c1, c2):
    seq = 'AKQJT98765432'
    i1 = seq.index(c1)
    i2 = seq.index(c2)
    if i1 < i2:
        return -1
    if i1 == i2:
        return 0
    return 1


def compare(h1, h2):
    l1 = hand_level(h1[0])
    l2 = hand_level(h2[0])

    if l1 < l2:
        return -1
    if l1 > l2:
        return 1

    for c1, c2 in zip(h1[0], h2[0]):
        cmp_k = compare_rank(c1, c2)
        if not cmp_k:
            continue
        return cmp_k
    return -1


hands_bids = []
for line in lines:
    h, b = line.split()
    hands_bids.append((h, int(b)))

sorted_hands = sorted(hands_bids, key=functools.cmp_to_key(compare), reverse=True)

ans = 0
for idx, (_, bid) in enumerate(sorted_hands):
    ans += (bid * (idx + 1))
print(ans)