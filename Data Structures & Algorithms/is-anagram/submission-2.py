class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        temp1 = []
        dict1 = {}
        dict2 = {}
        count = 0

        if len(s) != len(t):
            return False

        for c in s:
            temp1.append(c)
        
        for d in t:
            temp1.append(d)
        
        for char in s:
            dict1[char] = dict1.get(char, 0) + 1
        
        for char in t:
            dict2[char] = dict2.get(char, 0) + 1
        
        if dict1 == dict2:
            return True
        else: 
            return False


