"""
B - Trained?
url: https://atcoder.jp/contests/abc065/tasks/abc065_b

Problem Statement (my explanation)
 
You have a gym machine with N buttons (numbered 1 to N). Only one button is lit up at a time, starting with Button 1.
When you press a lit button, it turns off and a new button lights up according to a rule.
Your goal is to press the buttons in a way that eventually lights up Button 2.

How the Buttons Work
Initial State: Button 1 is lit up.

Pressing a Button:
If you press a lit button i, it turns off, and Button a[i] will light up next.
The sequence a[i] is given as input, which tells you which button lights up after pressing button i.
If you press a button that is not lit, nothing happens.

Input:
The first number is N, the total number of buttons.

The next N numbers describe the button light-up sequence: 
a[1],a[2],...,a[N].

Output:
Print -1 if you cannot light up Button 2.
If it's possible, print the minimum number of button presses needed to light up Button 2.

Constraints
- The number of buttons N can go up to 100,000.
- Each a[i] can point to any button between 1 and N.

Example
Input is 3 3 1 2
Here, we have 3 buttons.
The sequences mean:
Pressing Button 1 lights up Button 3.
Pressing Button 2 lights up Button 1.
Pressing Button 3 lights up Button 2.
Starting at Button 1:

Press Button 1 → Lights up Button 3.
Press Button 3 → Lights up Button 2.
Result: It takes 2 presses to reach Button 2.
"""
n, *seq = map(int, input().split())  # * operator for unpacking, which allows you to capture multiple values from an iterable
button_seq = tuple(seq)

# print("Number of buttons (N):", n)
# print("Sequence of button mappings (a):", button_seq)

current_button = 1  # coz we start with 1
press_count = 0

visited = set()

while current_button != 2:
    if current_button in visited:
        print(-1)  # we won't be able to reach button 2 
        break
    
    visited.add(current_button)
    # print(visited)
    
    current_button = button_seq[current_button - 1]
    press_count += 1

else:
    # we reached button 2
    print(press_count)