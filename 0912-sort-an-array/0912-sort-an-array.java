// class Solution {
//     public int[] sortArray(int[] nums) {
//         // int left=0;
//         // int right = nums.length-1;
//         // while(left<right){
//         //     if(nums[left]>nums[right]){
//         //         int temp = nums[left];
//         //         nums[left]= nums[right];
//         //         nums[right]= temp;
//         //     }
//         //     left++;
//         //     right--;
//         // }
//         // return nums;
//         // boolean swapped = true;
//         // while (swapped) {
//         //     swapped = false;
//         //     for (int i = 0; i < nums.length - 1; i++) {
//         //         if (nums[i] > nums[i + 1]) {
//         //             int temp = nums[i];
//         //             nums[i] = nums[i + 1];
//         //             nums[i + 1] = temp;
//         //             swapped = true;
//         //         }
//         //     }
//         // }
//         // return nums;
        
// //            for (int i = 0; i < nums.length - 1; i++) {
// //             for (int j = 0; j < nums.length - i - 1; j++) {
// //                 if (nums[j] > nums[j + 1]) {
// //                     int temp = nums[j];
// //                     nums[j] = nums[j + 1];
// //                     nums[j + 1] = temp;
// //                 }
// //             }
// //         }
// //         return nums;
    
//     }
// }



class Solution {
    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length - 1);
        return nums;
    }
    
    private void mergeSort(int[] nums, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            mergeSort(nums, left, mid);
            mergeSort(nums, mid + 1, right);
            merge(nums, left, mid, right);
        }
    }
    
    private void merge(int[] nums, int left, int mid, int right) {
        int[] temp = new int[nums.length];
        for (int i = left; i <= right; i++) {
            temp[i] = nums[i];
        }
        
        int i = left;
        int j = mid + 1;
        int k = left;
        
        while (i <= mid && j <= right) {
            if (temp[i] <= temp[j]) {
                nums[k++] = temp[i++];
            } else {
                nums[k++] = temp[j++];
            }
        }
        
        while (i <= mid) {
            nums[k++] = temp[i++];
        }
    }
}
