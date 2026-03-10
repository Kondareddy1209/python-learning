class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:
        # flower -> counts how many flowers we can place
        flower = 0
        
        # count -> counts continuous empty plots (0s)
        # initialized as 1 to handle the left boundary case
        count = 1

        # traverse through the flowerbed
        for r in range(len(nums)):
            
            # if the current plot is empty
            if nums[r] == 0:
                # increase the count of consecutive empty plots
                count += 1
            
            else:
                # if we encounter a flower (1),
                # calculate how many flowers can be placed in the
                # previous sequence of empty plots
                flower += (count - 1) // 2
                
                # reset count because the sequence of zeros breaks
                count = 0

        # handle the right boundary (end of array)
        count += 1
        
        # calculate flowers for the last sequence of empty plots
        flower += (count - 1) // 2

        # return True if we can place at least n flowers
        return flower >= n