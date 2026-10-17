class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dict1 = {}
        count = 0

        for num in nums:
            dict1[num] = dict1.get(num, 0) + 1

        for i, num in enumerate(dict1): 
            if dict1[num] > 1:
                count = 1
                break
            
            else:
                count = 0
        
        return bool(count)