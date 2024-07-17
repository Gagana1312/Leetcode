/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// class Solution {
//     public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
//         if (root == null || p == null || q == null) {
//             return null;
//         }
//         while (root != null) {
//             if (p.val > root.val && q.val > root.val) {
//                 root = root.right;
//             }
//             else if (p.val < root.val && q.val < root.val) {
//                 root = root.left;
//             }
//             else {
//                 return root;
//             }
//         }
//         return root;
//     }
// }

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // Base case: if root is null or root is one of p or q
        if (root == null || root == p || root == q) {
            return root;
        }

        // Recur for the left and right subtrees
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);

        // If both left and right are not null, root is the LCA
        if (left != null && right != null) {
            return root;
        }

        // Otherwise, return the non-null value
        return left != null ? left : right;
    }
}
