class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letter_dict_s = {}
        letter_dict_t = {}

        for char_s, char_t in zip(s, t):
            letter_dict_s[char_s] = letter_dict_s.get(char_s, 0) + 1
            letter_dict_t[char_t] = letter_dict_t.get(char_t, 0) + 1
        
        return letter_dict_s == letter_dict_t
        

            
                
        