class Solution {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        int[] res= new int[2];
        int diff = 0;
        for (int i = 0; i < numbers.length; i++) {
            diff = target - numbers[i];
            if(numMap.containsKey(diff)){
                res[0]= numMap.get(diff)+1;
                res[1] = i+1;
                return res;
            }
            numMap.put(numbers[i],i);

        }
        return res;
    }
}