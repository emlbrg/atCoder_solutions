"""
B - Hands on Ring (Easy)
url: https://atcoder.jp/contests/abc376/tasks/abc376_b
"""
max_value, queries = list(map(int, input().split()))
left_pos = 1
right_pos = 2
final_answer = 0
current_answer = 0

for _ in range(queries):
    line = input().split()
    move_target = int(line[1])
    hand_used = line[0]
    
    if hand_used == 'R':
        if (left_pos > right_pos) and (left_pos < move_target):
            current_answer = max_value - (move_target - right_pos)
        elif (left_pos > right_pos) and (left_pos == move_target):
            current_answer = 0
        elif (left_pos > right_pos) and (right_pos < move_target):
            current_answer = move_target - right_pos
        elif (left_pos > right_pos) and (right_pos == move_target):
            current_answer = 0
        elif (left_pos > right_pos) and (right_pos > move_target):
            current_answer = right_pos - move_target
        elif (left_pos < right_pos) and (right_pos < move_target):
            current_answer = move_target - right_pos
        elif (left_pos < right_pos) and (right_pos == move_target):
            current_answer = 0
        elif (left_pos < right_pos) and (left_pos < move_target):
            current_answer = right_pos - move_target
        elif (left_pos < right_pos) and (left_pos == move_target):
            current_answer = 0
        elif (left_pos < right_pos) and (left_pos > move_target):
            current_answer = max_value - (right_pos - move_target)
        right_pos = move_target
        
    elif hand_used == 'L':
        if (left_pos > right_pos) and (left_pos < move_target):
            current_answer = move_target - left_pos
        elif (left_pos > right_pos) and (left_pos == move_target):
            current_answer = 0
        elif (left_pos > right_pos) and (right_pos < move_target):
            current_answer = left_pos - move_target
        elif (left_pos > right_pos) and (right_pos == move_target):
            current_answer = 0
        elif (left_pos > right_pos) and (right_pos > move_target):
            current_answer = max_value - (left_pos - move_target)
        elif (left_pos < right_pos) and (right_pos < move_target):
            current_answer = max_value - (move_target - left_pos)
        elif (left_pos < right_pos) and (right_pos == move_target):
            current_answer = 0
        elif (left_pos < right_pos) and (left_pos < move_target):
            current_answer = move_target - left_pos
        elif (left_pos < right_pos) and (left_pos == move_target):
            current_answer = 0
        elif (left_pos < right_pos) and (left_pos > move_target):
            current_answer = left_pos - move_target
        left_pos = move_target

    final_answer += current_answer
    current_answer = 0

print(final_answer)




def num_move(n, from_, to, ng):
    if from_ > to:
        from_, to = to, from_
    if from_ < ng < to:
        return n + from_ - to
    else:
        return to - from_

n, q = map(int, input().split())
l, r = 1, 2
ans = 0

for _ in range(q):
    h, t = input().split()
    t = int(t)
    if h == 'L':
        ans += num_move(n, l, t, r)
        l = t
    else:
        ans += num_move(n, r, t, l)
        r = t

print(ans)
