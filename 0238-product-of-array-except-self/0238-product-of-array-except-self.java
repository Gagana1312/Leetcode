class Solution {
    public int[] productExceptSelf(int[] nums) {
        //works
        // int N = nums.length;
        // int[] left_prod = new int[N];
        // int[] right_prod = new int[N];

        // int[] res = new int[N];

        // left_prod[0] = 1;
        // right_prod[N-1] =1;

        // for (int i =1; i<N;i++){
        //     left_prod[i]  = nums[i-1]* left_prod[i-1];
        // }
        // for (int i=N-2;i>=0;i--){
        //     right_prod[i]  = nums[i+1] * right_prod[i+1];
        // }

        // for(int i=0;i<N;i++){
        //     res[i] = left_prod[i] * right_prod[i];
        // }
        // return res;
        int N = nums.length;
        int[] res = new int[N];

       res[0] = 1;

        for (int i =1; i<N;i++){
            res[i]  = nums[i-1]* res[i-1];
        }
        int temp =1;
        for (int i=N-1;i>=0;i--){
            res[i]  = res[i] * temp;
            temp = temp * nums[i];
        }

        return res;

    }
}