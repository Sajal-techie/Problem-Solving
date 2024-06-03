class Solution {
  int appendCharacters(String s, String t) {
    int index = 0;
    for (int i =0;i<s.length;i++){
        if (index < t.length){
            if (s[i]==t[index]){
                index++;
            }
        }
    }
    return t.length - index;
  }
}