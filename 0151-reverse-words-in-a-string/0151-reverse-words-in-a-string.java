class Solution {
    public String reverseWords(String s) {
        // String input = s.replaceAll("//s","");

        // StringBuilder out = new StringBuilder();
        // for(int i=input.length()-1;i>=0;i--){
        //     out.append(input.charAt(i));
        // }
        // return out.toString();

    //    String[] input = s.split(" ");
    //     List<String> list = new ArrayList<>(Arrays.asList(input));
    //     int left = 0;
    //     int right = list.size() - 1;

    //     while (left < right) {
    //         String temp = list.get(left);
    //         list.set(left, list.get(right));
    //         list.set(right, temp);
    //         left++;
    //         right--;
    //     }

    //     StringBuilder listString = new StringBuilder();
    //     for (int i = 0; i < list.size(); i++) {
    //         listString.append(list.get(i));
    //         if (i < list.size() - 1) {
    //             listString.append(" ");
    //         }
    //     }
    //     return listString.toString();


    // Split the input string by spaces, filter out empty strings
        String[] input = s.trim().split("\\s+");
        
        // Convert the array to a list for easier manipulation
        List<String> words = new ArrayList<>(Arrays.asList(input));
        
        // Reverse the list of words
        int left = 0;
        int right = words.size() - 1;
        while (left < right) {
            String temp = words.get(left);
            words.set(left, words.get(right));
            words.set(right, temp);
            left++;
            right--;
        }
        
        // Join the reversed list of words into a single string with spaces
        return String.join(" ", words);
    }
}