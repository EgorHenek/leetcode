/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ArrayList<Integer> postorderTraversal(TreeNode root) {
    
    
    
    ArrayList<Integer> arr =  new ArrayList<Integer>();
    Stack<Integer> parentStack = new Stack<Integer>();
    
    ListNode lastVisited = null;
    
    while(!parentStack.isEmpty() || root != null){
        if (root != null){
            parentStack.push(root);
            root = root.left;
        }else{
            ListNode peekNode = parentStack.peek();
            if (peekNode.right!=null && peekNode.right != lastVisited){
                root = peekNode.right;
            }else{
                parentStack.pop();
                arr.add(peekNode);
                lastVisited = peekNode;
            }
        }
            
    }
        
    }
}