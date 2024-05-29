class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1,mid=0;
        while (left < right){
            mid = (left+right) / 2;
        System.out.println(mid);
            if (nums[mid] < nums[right]){
                right = mid;
            }else{
                left = mid +1;
            }
        }
        return nums[left];
    }
}