class Solution {
    public boolean isPalindrome(String s) {
        // String input = s.replaceAll("\\s", "");
        // input = input.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        // int right = s.length()-1;
        // int left = 0;
        // Boolean result=false;
        // if(input.length()== 0){
        //     return result;
        // }
        // while(left<=right){
        //     if(input.charAt(left)==input.charAt(right)){
        //         return true;
        //     }
        //     left++;
        //     right--;
        // }
        // return result;
    //     boolean result = true;
    //     String input = s.replaceAll("\\s","");
	//     int length = input.length();
	//     for (int i = 0; i < length/2; i++) {
	// 	    if (input.charAt(i) != input.charAt(length - i - 1)) {
	// 		    result = false;
	// 		    break;
	// 	}
	// }
    // return result;


    // Remove all spaces
        String input = s.replaceAll("\\s", "");
        // Remove all non-alphanumeric characters and convert to lowercase
        input = input.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        
        int length = input.length();
        for (int i = 0; i < length / 2; i++) {
            if (input.charAt(i) != input.charAt(length - i - 1)) {
                return false;
            }
        }
        
        return true;
    }
}