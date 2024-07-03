class Solution {
    public int lengthOfLongestSubstring(String s) {
        // HashSet<String> ls = new HashSet();
        // int count =0;
        // int left = 0;

        // for(int i=0;i<s.length();i++){
        //     while(int s[right]: ls){
        //         ls.remove(s[left]);
        //         left++;
        //     }
        //     ls.add(s[right]);
        //     count= math.max(count, right-left+1);
        // }
        // return count;  

        int maxlength = 0 ;
        for(int i=0;i<s.length();i++){
            StringBuilder currsub = new StringBuilder();
            for (int j = i; j < s.length();j++){
                if(currsub.indexOf(String.valueOf(s.charAt(j))) != -1 ){
                    break;
                }
                currsub.append(s.charAt(j));
                maxlength = Math.max(maxlength,currsub.length());

            }

        }
        return maxlength;

    }
}
