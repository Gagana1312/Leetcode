class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        List<Integer> cur = new ArrayList();
        dfs(0,cur,ans, candidates, target);
        return ans;
        
    }
    private void dfs(int index, List<Integer> cur, List<List<Integer>> ans, int[] candidates, int target){
        if(target ==0){
            ans.add(new ArrayList(cur));
        } else if (target < 0 || index >= candidates.length){
            return;
        }else{
            cur.add(candidates[index]);
            dfs(index,cur,ans,candidates,target-candidates[index]);

            cur.remove(cur.get(cur.size()-1));
            dfs(index+1,cur,ans,candidates,target);
        }
    }
}