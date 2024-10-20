class Solution {
    public boolean parseBoolExpr(String expression) {
        Stack<Character> stack = new Stack<>();
        for (char c: expression.toCharArray()) {
            if (c ==')') {
                Set<Character> set = new HashSet<>();
                while (stack.peek() != '(') {
                    set. add(stack.pop());
                }
                stack. pop(); // pop '(*
                char operator = stack.pop();
                if (operator == '!') {
                    stack. push(set.contains('f')? 't' : 'f');
                } else if (operator == '&') {
                    stack.push(set.contains('f')? 'f' : 't');
                } else if (operator == '|') {
                    stack.push(set.contains('t')? 't' : 'f');
                }
                
            } else if (c !=',') {
                stack.push(c);
            }
        }
        return stack.pop() == 't';
        
    }
}