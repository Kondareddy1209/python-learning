# Reverse Words in a String
# Problem: Given a string, reverse the order of words.

# ------------------------------------------------
# Solution 1: Two Pointer Swap Method
# ------------------------------------------------

class SolutionSwap:
    def reverseWords(self, s: str) -> str:
        # split() removes extra spaces and converts string into list
        # Example: "  hello world  " -> ['hello','world']
        n = s.split()

        # initialize two pointers
        l = 0
        r = len(n) - 1

        # swap words until pointers meet
        while l < r:
            n[l], n[r] = n[r], n[l]
            l += 1
            r -= 1

        # convert list back to string
        return " ".join(n)


# ------------------------------------------------
# Solution 2: Reverse Traversal Method
# ------------------------------------------------

class SolutionLoop:
    def reverseWords(self, s: str) -> str:
        # convert string to list of words
        n = s.split()

        # empty string to store result
        res = ""

        # traverse from last word to first word
        for i in range(len(n)-1, -1, -1):
            res += n[i]

            # add space between words
            if i != 0:
                res += " "

        return res


# ------------------------------------------------
# Example Test
# ------------------------------------------------

s = "  hello world  "

print("Swap Method:", SolutionSwap().reverseWords(s))
print("Loop Method:", SolutionLoop().reverseWords(s))