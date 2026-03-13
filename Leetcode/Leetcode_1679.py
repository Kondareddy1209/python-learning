from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Problem:
        Find the maximum number of pairs in the array such that
        the sum of each pair equals k. Each element can be used only once.

        Approach (Two Pointer Technique):
        1. First sort the array so that we can use two pointers.
        2. Use two pointers:
           - l (left) starting from the beginning.
           - r (right) starting from the end.
        3. Check the sum of elements at these pointers.
        4. If sum == k → we found a valid pair:
              - increase pair count
              - move both pointers inward
        5. If sum < k → move the left pointer right to increase the sum.
        6. If sum > k → move the right pointer left to decrease the sum.
        7. Continue until the pointers meet.

        Why this works:
        Sorting allows us to efficiently adjust the sum by moving pointers
        instead of checking all possible pairs (which would be O(n²)).

        Time Complexity (TC):
        Sorting takes O(n log n)
        Two-pointer traversal takes O(n)
        Overall TC = O(n log n)

        Space Complexity (SC):
        O(1) → No extra data structures used (in-place operations)
        """

        pairs = 0                # Count of valid pairs
        nums.sort()              # Sort the array to apply two-pointer technique

        l = 0                    # Left pointer
        r = len(nums) - 1        # Right pointer

        # Continue until the two pointers meet
        while l < r:

            n = nums[l] + nums[r]   # Current pair sum

            if k == n:              # If the pair sum equals k
                pairs += 1          # Found a valid pair
                l += 1              # Move left pointer forward
                r -= 1              # Move right pointer backward

            elif n < k:             # If sum is smaller than k
                l += 1              # Increase sum by moving left pointer

            else:                   # If sum is greater than k
                r -= 1              # Decrease sum by moving right pointer

        return pairs               # Return total number of valid pairs