from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Problem
        -------
        Given an array `height` where each element represents the height of a vertical line,
        find two lines that together with the x-axis form a container that holds the most water.

        Example
        -------
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49

        Explanation:
        The container formed by height[1] = 8 and height[8] = 7 gives the maximum area.

        --------------------------------------------------

        Approach: Two Pointer Technique
        --------------------------------
        1. Start with two pointers:
           - Left pointer (l) at the beginning.
           - Right pointer (r) at the end.
        2. Calculate the width between them.
        3. The height of the container is determined by the shorter line.
        4. Area = width × minimum height of the two lines.
        5. Update the maximum area found so far.
        6. Move the pointer pointing to the smaller height inward because:
           - Moving the taller line will not increase the area.
           - We try to find a taller line to increase the container height.
        7. Continue until both pointers meet.

        Why This Works
        ---------------
        The width decreases as pointers move inward, so we try to increase the height
        by moving the pointer at the smaller height.

        --------------------------------------------------

        Time Complexity
        ----------------
        O(n) → We traverse the array once using two pointers.

        Space Complexity
        -----------------
        O(1) → No extra space is used.
        """

        l = 0                       # Left pointer
        r = len(height) - 1         # Right pointer
        ans = 0                     # Stores maximum water area

        while l < r:
            width = r - l                           # Distance between lines
            h = min(height[l], height[r])           # Container height determined by smaller line

            ans = max(ans, width * h)               # Update maximum area

            # Move pointer with smaller height
            if height[l] < height[r]:
                l += 1                              # Move left pointer to try a taller line
            else:
                r -= 1                              # Move right pointer to try a taller line

        return ans                                  # Return maximum water area