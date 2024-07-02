class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int area = 0;

        while (left < right){
            int max_area = Math.min(height[right], height[left])*(right-left);
            area = Math.max(area, max_area);
            if(height[left] < height[right]){
                left++;
            } else {
                right--;
            }
        }

        return area;
    }
}