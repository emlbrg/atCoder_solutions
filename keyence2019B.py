"""
B - KEYENCE String
url: https://atcoder.jp/contests/keyence2019/tasks/keyence2019_b

A string is called a KEYENCE string when it can be changed to keyence by removing its contiguous substring (possibly empty) only once.
Example: keyofscience
Output: YES
Example 2: mpyszsbznf
Output: NO

Given a string S consisting of lowercase English letters, determine if S is a KEYENCE string.

Constraints
The length of S is between 7 and 100 (inclusive).
S consists of lowercase English letters.
"""
def is_keyence_string(S: str) -> str:
    keyence = 'keyence'
    n = len(S)
    m = len(keyence)
    
    j = 0 
    for i in range(n):
        if j < m and S[i] == keyence[j]:
            j += 1
        if j == m:  # atched all characters in keyence
            return 'YES'
    
    return 'NO'

""" Other implementation """
# S = input().strip()
# print(is_keyence_string(S))

# S = input()
# word = 'keyence'
# len_word = len(word)

# for i in range(len_word + 1):
#     up = word[:i]
#     bo = word[i:]
#     if S[:i] == up and S[-len(bo):] == bo:
#         print('YES')
#         break
# else:
#     print('NO')