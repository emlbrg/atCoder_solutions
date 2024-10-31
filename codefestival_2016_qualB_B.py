"""
B - Qualification simulator
url: https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_b

Inputs:
N: Total number of participants.
A: Maximum number of Japanese students that can pass.
B: Maximum number of overseas students that can pass.
S: A string of length N where each character indicates the type of participant:
'a': Japanese student.
'b': Overseas student.
'c': Neither (cannot pass).

Conditions for Passing:
Japanese students ('a') can pass if the total number of students who have passed so far is less than A + B.
Overseas students ('b') can pass if:
The total number of passed students is less than A + B.
They are within the top B overseas students.

Goal:
For each participant, determine if they passed or not.
"""
def qualification_results(N, A, B, S):
    total_passed = 0
    overseas_passed = 0
    results = []

    for participant in S:
        if participant == 'a':  # 日本人
            if total_passed < A + B:
                results.append("Yes")
                total_passed += 1
            else:
                results.append("No")
        elif participant == 'b':  # 外国人
            if total_passed < A + B and overseas_passed < B:
                results.append("Yes")
                total_passed += 1
                overseas_passed += 1
            else:
                results.append("No")
        else:
            results.append("No")  # 学生ではない

    print("\n".join(results))

N, A, B = map(int, input().split())
S = input().strip()

qualification_results(N, A, B, S)