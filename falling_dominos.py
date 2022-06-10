'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:

L, meaning the domino has just been pushed to the left,
R, meaning the domino has just been pushed to the right, or
., meaning the domino is standing still.
Determine the orientation of each tile when the dominoes stop falling. Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.

For example, given the string .L.R....L, you should return LL.RRRLLL.

Given the string ..R...L.L, you should return ..RR.LLLL.
'''

def pushDominoes(dominoes):
    N = len(dominoes)
    force = [0] * N

    # Populate forces going from left to right
    f = 0
    for i in range(N):
        if dominoes[i] == 'R': 
            f = N
        elif dominoes[i] == 'L': 
            f = 0
        else: 
            f = max(f-1, 0)
        force[i] += f

    # Populate forces going from right to left
    f = 0
    for i in range (N-1, -1, -1):
        if dominoes[i] == 'L': 
            f = N
        elif dominoes[i] == 'R': 
            f = 0
        else: 
            f = max(f-1, 0)
        force[i] -= f

    return "".join('.' if f==0 else 'R' if f > 0 else 'L'
                    for f in force)

print(pushDominoes(".L.R....L"))
print(pushDominoes("..R...L.L"))

'''
Intuition

We can calculate the net force applied on every domino. The forces we care about are how close a domino is to a leftward 'R', and to a rightward 'L': the closer we are, the stronger the force.

Algorithm

Scanning from left to right, our force decays by 1 every iteration, and resets to N if we meet an 'R', so that force[i] is higher (than force[j]) if and only if dominoes[i] is closer (looking leftward) to 'R' (than dominoes[j]).

Similarly, scanning from right to left, we can find the force going rightward (closeness to 'L').

For some domino answer[i], if the forces are equal, then the answer is '.'. Otherwise, the answer is implied by whichever force is stronger.

Example

Here is a worked example on the string S = 'R.R...L': We find the force going from left to right is [7, 6, 7, 6, 5, 4, 0]. The force going from right to left is [0, 0, 0, -4, -5, -6, -7]. Combining them (taking their vector addition), the combined force is [7, 6, 7, 2, 0, -2, -7], for a final answer of RRRR.LL.
'''