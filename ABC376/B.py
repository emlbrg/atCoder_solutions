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

