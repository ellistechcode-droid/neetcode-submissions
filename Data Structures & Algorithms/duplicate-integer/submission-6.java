class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> hashy = new HashSet<>();

        for(int i : nums) {
            if(hashy.contains(i)){
                return true;
            }
            hashy.add(i);
        }
        return false;
    }
}