class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> hasho = new HashSet<>();

        for(int i = 0; i < nums.length; i++) {
            if(hasho.contains(nums[i])){
                return true;
            } else {
                hasho.add(nums[i]);
            }
        }
        return false;
    }
}