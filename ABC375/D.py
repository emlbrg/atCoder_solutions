S = input()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

positions = {char: [] for char in alphabet}  # type: ignore

for i, char in enumerate(S):
    positions[char].append(i)

def count_pairs(list):
    list_len = len(list)
    ret = 0
    for i in range(1, list_len):
        start = list[i-1]
        end = list[i]
        ret += i * (list_len - i) * (end - start-1)
    for i in range(list_len):
        ret += i * (list_len - i -1)
    return ret

cunt = 0
for char in alphabet:
    cunt += count_pairs(positions[char])
print(cunt)