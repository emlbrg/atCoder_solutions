"""
B - Unvarnished Report
url: https://atcoder.jp/contests/abc374/tasks/abc374_b

You are given two strings S and T, consisting of lowercase English letters.
If S and T are equal, print 0; otherwise, print the position of the first character where they differ.

Constraints
S and T are strings of length between 1 and 100, inclusive, consisting of lowercase English letters.

Sample Input 1

abcde
abedc

Sample Output 1

3
We have S= abcde and T= abedc.
S and T have the same first and second characters, but differ at the third character, so print 3.
"""
s1 = input().strip()
s2 = input().strip()

if s1 == s2:
    print('0')
else:
    min_length = min(len(s1), len(s2))
    for index in range(min_length):
        if not s1[index] == s2[index]:
            print(index + 1)
            break
    else:  # if we are here it's because the two strings are not the same length and that is the first difference
        print(min_length + 1)