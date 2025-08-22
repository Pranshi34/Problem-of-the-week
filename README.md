Problems of the week
1. Greatest Common Divisor (GCD) of n Numbers
Problem: Given n numbers, find the GCD of all of them.

Logic:

Start with the first number as initial GCD.
Iteratively update the GCD with the next number using math.gcd().
Time Complexity: O(n × log(min(a, b))) → for n numbers.
Space Complexity: O(1) (no extra space).

2. Count Unival Subtrees
Problem: Count how many subtrees in a binary tree are "unival" (all nodes have the same value).

Logic:

Use recursion (DFS).
For each node:
Check if both left and right subtrees are unival.
Check if node’s value matches children values.
Single nodes are always unival.
Time Complexity: O(n) → visits each node once.
Space Complexity: O(h) → recursion stack, h = tree height.

3. Word Search in a Matrix (Horizontal & Vertical)
Problem: Check if a word exists in a 2D matrix either left-to-right (row-wise) or top-to-bottom (column-wise).

Logic:

Traverse each row, join characters, and check if the word is a substring.
Traverse each column the same way.
Time Complexity: O(M × N) → scanning matrix.
Space Complexity: O(max(M, N)) → storing row/column string.

4. Partition Equal Subset Sum
Problem: Given a list of integers, check if it can be split into two subsets with equal sum.

Logic:

If total sum is odd → return False.
Else use Dynamic Programming (Subset Sum): check if a subset sums to half of total.
Time Complexity: O(n × target), where target = total_sum / 2.
Space Complexity: O(target) → 1D DP array.

5. Input Handling for Matrix & Word Search
Problem: Accept matrix and word from user input, then check word presence.

Logic:

First take M (rows), N (cols).
Input each row as characters.
Input the word to search.
Apply word search logic.
Time Complexity: Same as problem 3 → O(M × N).
Space Complexity: Same as problem 3 → O(max(M, N)).

6. Input Handling for Partition Equal Subset Sum
Problem: Accept list from user and check if partition possible.

Logic:

Input list of integers.
Use DP-based solution (same as problem 4).
Time Complexity: Same as problem 4 → O(n × target).
Space Complexity: Same as problem 4 → O(target).
