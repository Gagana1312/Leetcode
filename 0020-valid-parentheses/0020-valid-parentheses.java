class Solution {
    public boolean isValid(String s) {
        Stack<Character> bracks = new Stack<>();
        Map<Character,Character> closers = new HashMap<>(3);

        closers.put(')','(');
        closers.put(']','[');
        closers.put('}','{');
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(closers.containsKey(c)) {
                if(!bracks.isEmpty() && closers.get(c).equals(bracks.peek())) {
                    bracks.pop();
                } else {
                    return false;
                }
            }else{
                bracks.push(c);
            }
        }
        return bracks.isEmpty();



        // Stack<Character> brackets = new Stack<>();
        // Map<Character, Character> bracketLookup = new HashMap<>(3);

        // bracketLookup.put(')', '(');
        // bracketLookup.put('}', '{');
        // bracketLookup.put(']', '[');

        // for (int i = 0; i < s.length(); i++) {
        //     char c = s.charAt(i);
        //     if (bracketLookup.containsKey(c)) {
        //         if (!brackets.isEmpty() && bracketLookup.get(c).equals(brackets.peek())) {
        //             brackets.pop();
        //         } else {
        //             return false;
        //         }
        //     } else {
        //         brackets.push(c);
        //     }
        // }

        // return brackets.isEmpty();
    }
}