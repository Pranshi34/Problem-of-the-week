### Problems of the week


## 1.Minimum Number of Perfect Squares (DP)
**Problem:**
Given an integer n, find the minimum number of perfect square numbers that sum up to n.


**Logic:**  
- Precompute all perfect squares ≤ n. 

- Use Dynamic Programming (DP):
               dp[i] = minimum number of perfect squares that sum to i.  

**Time Complexity:** O(n * √n) → for each i up to n, we try all possible square numbers.
**Space Complexity:** O(n) → to store the DP array.




## 2.Misère Nim Game
**Problem:**
You are given heaps of stones. Two players alternate turns. On each turn, a player removes one or more stones from exactly one heap.
The player who takes the last stone loses (misère Nim).
Given heap sizes, decide whether the first player can force a win.


**Logic:**  
- Case 1: All heaps contain only 1 stone
             If the number of heaps is even, the first player wins.
             If the number of heaps is odd, the first player loses.

- Case 2: At least one heap has ≥ 2 stones
                Use the normal Nim rule:
                Compute xor_sum = heap1 ^ heap2 ^ heap3 ...
                If xor_sum != 0 → first player wins.
                Else → first player loses.  

**Time Complexity:** O(n) → compute XOR across all heaps.
**Space Complexity:** O(1) → only need to store XOR value.




## 3.Maximum Path Sum in a Binary Tree
**Problem:**
Find the maximum path sum between any two nodes in a binary tree.
A path can start and end at any nodes, but each node can appear only once.

**Logic:**  
- Use DFS (post-order traversal):
  For each node:
            Get maximum path sum from left child (ignore negatives).
            Get maximum path sum from right child (ignore negatives).
            Compute current_sum = node.val + left + right.
            Update a global maximum with current_sum.
            Return to parent: node.val + max(left, right) (choose one side).

- The global maximum is the final answer. 

**Time Complexity:** O(N) → each node is visited once.
**Space Complexity:** O(H) → recursion stack, where H is tree height.
                        Worst case (skewed tree): O(N)
                        Best case (balanced tree): O(log N)


