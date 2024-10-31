"""
B - Bingo
url: https://atcoder.jp/contests/abc157/tasks/abc157_b
"""
def check_bingo(bingo_card, chosen_numbers):
    chosen_set = set(chosen_numbers)
    
    marked = [[bingo_card[i][j] in chosen_set for j in range(3)] for i in range(3)]
    
    for i in range(3):
        if all(marked[i]):
            return "Yes"
        if all(marked[j][i] for j in range(3)):
            return "Yes"
    
    if all(marked[i][i] for i in range(3)):
        return "Yes"
    if all(marked[i][2 - i] for i in range(3)):
        return "Yes"
    
    return "No"

bingo_card = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
chosen_numbers = [int(input()) for _ in range(N)]

print(check_bingo(bingo_card, chosen_numbers))
