class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for r in range(len(s)):
            word = self.checkPalindrome(s, r)
            # print(f"word = {word}")
            if len(word) >= len(ans):
                ans = word

        return ans

    def checkPalindrome(self, s, idx):
        # case 1: i-1, i+1
        k = 0
        word1 = ""
        while(idx-k >= 0 and idx+k < len(s) and s[idx-k] == s[idx+k]):
            # record
            word1 = s[idx-k:idx+k+1]
            # print(f"idx = {idx}, k = {k}, word1 = {word1}") # debug
            # move to next
            k += 1 


        # case 2: i, i+1
        k = 0
        word2 = ""
        while(idx-k >= 0 and (idx+1)+k < len(s) and s[idx-k] == s[(idx+1)+k]):
            # record
            word2 = s[idx-k:(idx+1)+k+1]
            # print(f"idx = {idx}, k = {k}, word2 = {word2}") # debug
            # move to next
            k += 1 

        # return longest word(substring)
        if len(word1) >= len(word2):
            return word1
        else:
            return word2