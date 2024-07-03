class Solution {
    public int characterReplacement(String s, int k) {
        char[] arr = s.toCharArray();
        int left =0, right=0, n= arr.length;

        HashMap<Character, Integer> map = new HashMap<>();

        int maxlength=0, maxfreq=0;

        while(right < n){
            map.put(arr[right], map.getOrDefault(arr[right],0)+1);
            maxfreq = Math.max(maxfreq, map.get(arr[right]));

            if((right-left+1)-maxfreq > k){
                map.put(arr[left],map.get(arr[left])-1);
                left++;
            }
            maxlength = Math.max(maxlength, right-left+1);
            right++;
        }
        return maxlength;
    }
}