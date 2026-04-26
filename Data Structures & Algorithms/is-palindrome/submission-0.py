class Solution:
    def isPalindrome(self, s: str) -> bool:

        sentence = "".join(char.lower() for char in s if char.isalnum())
        j = len(sentence) - 1

        for i in range(len(sentence)):
            if sentence[i] != sentence[j]:
                return False
            j -= 1
        
        return True
        