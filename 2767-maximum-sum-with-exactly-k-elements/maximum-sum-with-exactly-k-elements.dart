class Solution {
  int maximizeSum(List<int> nums, int k) {
    int value = nums.reduce(max) ;
    int ans = 0;
    for (int i=0;i<k;i++){
        value ++;
        ans = ans + value;
    }
    return ans - k;
  }
}