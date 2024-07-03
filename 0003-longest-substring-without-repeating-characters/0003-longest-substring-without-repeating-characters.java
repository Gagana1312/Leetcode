class Solution {
    public int lengthOfLongestSubstring(String s) {

        // Works
        // int maxlength = 0 ;
        // for(int i=0;i<s.length();i++){
        //     StringBuilder currsub = new StringBuilder();
        //     for (int j = i; j < s.length();j++){
        //         if(currsub.indexOf(String.valueOf(s.charAt(j))) != -1 ){
        //             break;
        //         }
        //         currsub.append(s.charAt(j));
        //         maxlength = Math.max(maxlength,currsub.length());

        //     }

        // }
        // return maxlength;

        int maxlength =0;
        HashMap<Character, Integer> visited = new HashMap<>();
        for (int right = 0,left = 0; right< s.length();right++){
            char currchar = s.charAt(right);
            if(visited.containsKey(currchar) && visited.get(currchar) >= left){
                left = visited.get(currchar)+1;
            }
            maxlength = Math.max( maxlength, right-left+1);
            visited.put(currchar,right);
        }
        return maxlength;
    }
}
