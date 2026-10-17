class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> numMap;

        for(int i = 0; i< nums.size(); i++){
            if(numMap.find(nums[i]) == numMap.end()){
                numMap[nums[i]] = i;
            } else {
                return true;
            }

            
        }
        


        return false;
    }
};