class Solution {
  int scoreOfString(String s) {
    int ans = 0;
    for (int i =0;i<s.length-1;i++){
        ans += (s.codeUnitAt(i) - s.codeUnitAt(i+1)).abs() ;
    }
    return ans;
  }
}