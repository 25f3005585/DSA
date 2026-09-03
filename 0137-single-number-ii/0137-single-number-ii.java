class Solution {
     public int singleNumber(int[] nums) {
        int once = 0, twice = 0;
        
        for (int num : nums) {
            once = (once ^ num) & ~twice;
            twice = (twice ^ num) & ~once; 
        }
        return once; 
    }
}