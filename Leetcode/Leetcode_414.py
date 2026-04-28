from typing import List

class Solution:
    """
    LeetCode 414: Third Maximum Number

    Approach (User's Logic):
    - Create a new list to store unique elements
    - Iterate through nums and append only distinct values
    - Sort the list
    - If less than 3 unique elements → return maximum
    - Else → return third maximum

    Time Complexity: O(n^2)  (due to 'not in' check)
    Space Complexity: O(n)
    """

    def thirdMax(self, nums: List[int]) -> int:
        unique_list = []

        # Remove duplicates manually
        for num in nums:
            if num not in unique_list:
                unique_list.append(num)

        # Sort the unique elements
        unique_list.sort()

        n = len(unique_list)

        # Return result
        if n < 3:
            return max(unique_list)
        else:
            return unique_list[-3]


if __name__ == "__main__":
    # Sample test cases
    solution = Solution()

    print(solution.thirdMax([3, 2, 1]))        # Expected Output: 1
    print(solution.thirdMax([1, 2]))           # Expected Output: 2
    print(solution.thirdMax([2, 2, 3, 1]))     # Expected Output: 1