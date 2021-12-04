class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        top_element=''
        stack=[]
        mapping={')':'(',']':'[','}':'{'}
        for char in s:
            if char in mapping:
                if stack:
                    top_element=stack.pop()
                else:
                    '#'
                if mapping[char]!=top_element:
                    return False
            else:
                stack.append(char)
        return not stack