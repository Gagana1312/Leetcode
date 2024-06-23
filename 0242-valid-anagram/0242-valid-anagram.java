class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        int[] hmap = new int[26];

        for (int i=0;i<s.length();i++){
            hmap[s.charAt(i)-'a']++;
            hmap[t.charAt(i)-'a']--;
        }

        for(int n:hmap) if(n!=0) return false;

        return true;

        
    }
}