/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null && q==null){
            return true;
        }
        if(p!=null && q!=null && p.val == q.val){
            return (isSameTree(p.left,q.left) && isSameTree(p.right,q.right));

        }else{
            return false;
        }
        
    }
}


// if not p and not q:
//             return True
        
//         if p and q and p.val == q.val:
//             return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
//         else:
//             return False
        