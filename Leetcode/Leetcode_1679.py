from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Problem
        -------
        Given an integer array `nums` and an integer `k`, return the maximum number 
        of operations where each operation consists of choosing two numbers whose 
        sum equals `k`. Each number can be used only once.

        Example
        -------
        Input: nums = [1,2,3,4], k = 5
        Output: 2
        Explanation:
        (1,4) -> 5
        (2,3) -> 5

        --------------------------------------------------

        Approach: Two Pointer Technique
        --------------------------------
        1. First sort the array so that numbers are in increasing order.
        2. Use two pointers:
           - Left pointer (l) starting from the beginning.
           - Right pointer (r) starting from the end.
        3. Calculate the sum of elements at both pointers.
        4. If the sum equals k:
              - A valid pair is found.
              - Increase the pair count.
              - Move both pointers inward.
        5. If the sum is less than k:
              - Move the left pointer forward to increase the sum.
        6. If the sum is greater than k:
              - Move the right pointer backward to decrease the sum.
        7. Continue until the pointers meet.

        Why This Works
        ---------------
        Sorting allows us to efficiently adjust the sum using two pointers 
        instead of checking every possible pair.

        --------------------------------------------------

        Time Complexity
        ----------------
        Sorting: O(n log n)
        Two-pointer traversal: O(n)

        Overall TC = O(n log n)

        Space Complexity
        -----------------
        O(1) → No extra space is used (in-place operations).
        """

        pairs = 0
        nums.sort()              # Sort array to apply two-pointer technique

        l = 0                    # Left pointer
        r = len(nums) - 1        # Right pointer

        # Traverse until both pointers meet
        while l < r:
            current_sum = nums[l] + nums[r]

            if current_sum == k:     # Valid pair found
                pairs += 1
                l += 1               # Move left pointer forward
                r -= 1               # Move right pointer backward

            elif current_sum < k:    # Sum too small → increase it
                l += 1

            else:                    # Sum too large → decrease it
                r -= 1

        return pairs