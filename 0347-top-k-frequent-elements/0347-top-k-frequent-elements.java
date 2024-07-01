class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        // count the frequency
        for(int i :nums){
            map.put(i, map.getOrDefault(i,0)+1);
        }
        //create a priority queue
        PriorityQueue<Map.Entry<Integer, Integer>> pq= 
        new PriorityQueue <>((a,b) -> b.getValue() - a.getValue());

        //add the number:frequency pair to priority queue.
        for(Map.Entry entry :map.entrySet()){
            pq.add(entry);
        } 
        //create a result list.
        int[] res = new int[k]  ;     
        // extract the top k elements from teh prioriity queue.
        for (int i=0;i<k;i++){
            res[i] =  pq.poll().getKey();
        }
        return res;
    }
}