import java.util.HashMap;

class LeetCode1 {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer, Integer> hash = new HashMap<>();
        int diff=0;
        for (int i = 0; i<nums.length;i++){
            diff = target-nums[i];
            if (hash.containsKey(diff))return new int[] {i,hash.get(diff)};
                hash.put(nums[i],i);
                
                
                 
             
        } return null;
    }
}
//Leetcode 1. TwoSum 
//Case -> nums = [2,7,11,15] -> [1,0]