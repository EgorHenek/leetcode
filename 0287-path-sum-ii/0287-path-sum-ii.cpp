/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int> > output;
    vector<vector<int> > pathSum(TreeNode *root, int sum)
    {
        vector<int> temp;
        int out;
        if(root == NULL)
            return output;
        findsum(temp,sum,0,root);
        return output;
    }
    
    void findsum(vector<int> &temp, int sum, int out, TreeNode *cur)
    {
        if(cur->left==NULL && cur->right==NULL && out+cur->val == sum)
        {
            temp.push_back(cur->val);
            output.push_back(temp);
            return;
        }
        TreeNode *current= cur;
        if(current->left!=NULL)
        {
            out+=current->left->val;
            if(out<=sum)
            {
                temp.push_back(current->left->val);
                findsum(temp,sum,out,current->left);
                temp.pop_back();
            }
        }
        if(current->right!=NULL)
        {
            out+=current->right->val;
            if(out<=sum)
            {
            temp.push_back(current->right->val);
            findsum(temp,sum,out,current->right);
            temp.pop_back();
            }
    
        }
        
    }
    
};