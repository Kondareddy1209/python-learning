from typing import List
from collections import Counter

class Solution:
    """
    LeetCode 1748: Sum of Unique Elements

    Approach (User's Logic):
    - Use Counter to store frequency of each element
    - Traverse the original list
    - Add elements whose frequency is exactly 1

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def sumOfUnique(self, nums: List[int]) -> int:
        # Count frequency of each number
        freq = Counter(nums)

        total = 0

        # Sum elements that appear only once
        for num in nums:
            if freq[num] == 1:
                total += num

        return total


if __name__ == "__main__":
    # Sample test cases
    solution = Solution()

    print(solution.sumOfUnique([1, 2, 3, 2]))        # Expected Output: 4
    print(solution.sumOfUnique([1, 1, 1, 1, 1]))     # Expected Output: 0
    print(solution.sumOfUnique([1, 2, 3, 4, 5]))     # Expected Output: 15