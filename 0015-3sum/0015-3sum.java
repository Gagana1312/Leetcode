// class Solution {
//     public List<List<Integer>> threeSum(int[] nums) {
//         List<List<Integer>> list = new ArrayList<List<Integer>>();
//         int[] res = new int[3];
//         for (int i=0;i<nums.length;i++){
//             for(int j=i+1;j<nums.length;j++){
//                 for(int k=j+1;k<nums.length;k++){
//                     if(i!=j && j!=k && i!=k){
//                         int summ = nums[i]+nums[k]+nums[j];
//                         if (summ == 0){
//                             res[0]= nums[i];
//                             res[1]= nums[j];
//                             res[2] = nums[k];
//                         }
//                         list.put(res);
//                     }
//                 }
//             }
//         }
//         return list;
//     }
// }


// class Solution {
//     public List<List<Integer>> threeSum(int[] nums) {
//         List<List<Integer>> result = new ArrayList<>();
//         Set<String> seen = new HashSet<>();

//         for (int i = 0; i < nums.length; i++) {
//             for (int j = i + 1; j < nums.length; j++) {
//                 for (int k = j + 1; k < nums.length; k++) {
//                     if (nums[i] + nums[j] + nums[k] == 0) {
//                         List<Integer> triplet = Arrays.asList(nums[i], nums[j], nums[k]);
//                         Collections.sort(triplet);
//                         String key = triplet.toString();
//                         if (!seen.contains(key)) {
//                             result.add(triplet);
//                             seen.add(key);
//                         }
//                     }
//                 }
//             }
//         }

//         return result;
//     }
// }



class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> output = new ArrayList<>();
        Arrays.sort(nums);

        for(int i =0;i<nums.length -2;i++){
            int start =i+1;
            int end = nums.length-1;

            if(i==0 || nums[i]!=nums[i-1]){
                while(start<end){
                int summ = nums[i]+nums[start]+nums[end];
                if(summ==0){
                    output.add(Arrays.asList(nums[i],nums[start],nums[end]));
                    while(start<end && nums[start] == nums[start+1]) start++;
                    while(start<end && nums[end] == nums[end-1]) end--;
                    start++;
                    end--;

                } else if( summ > 0){
                    end--;
                } else {
                    start++;
                }
            }

            }

            
        }
        return output;
    }
}