class Solution {
    public int[] productExceptSelf(int[] nums) {
        // int[] res = new int[10];
        // int prod = 1;
        // for(int i =0 ; i< nums.length-1;i++){
        //     if(i==0){
        //         for(int j=i;j<nums.length-i;j++){
        //             prod*=nums[j];
        //         }
        //     } else {
        //         for(int j=i;j<nums.length-i;j++){
        //             prod*=nums[j];
        //         }
        //         for (int j=0;j<i;j++){
        //             prod*=nums[j];
        //         }

        //     }
        //     res.append(prod);
        //     prod=1;
        // }

        int N = nums.length;
        int[] left_prod = new int[N];
        int[] right_prod = new int[N];

        int[] res = new int[N];

        left_prod[0] = 1;
        right_prod[N-1] =1;

        for (int i =1; i<N;i++){
            left_prod[i]  = nums[i-1]* left_prod[i-1];
        }
        for (int i=N-2;i>=0;i--){
            right_prod[i]  = nums[i+1] * right_prod[i+1];
        }

        for(int i=0;i<N;i++){
            res[i] = left_prod[i] * right_prod[i];
        }
        return res;

    }
}