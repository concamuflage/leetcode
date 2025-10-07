/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
let maxDepth = function (root) {
  if (root === null) {
    return 0;
  }
  return _recurCount(0, root);
};

const _recurCount = (count, root) => {
  if (root === null) {
    return count;
  }
  let count1 = _recurCount((count += 1), root.left);
  let count2 = _recurCount((count += 1), root.right);
  return max(count1, count2);
};

class TreeNode {
  constructor(val = 0, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

// Example test tree
let node7 = new TreeNode(7);
let node15 = new TreeNode(15);
let node20 = new TreeNode(20, node15, node7);
let node9 = new TreeNode(9);
let node3 = new TreeNode(3, node9, node20);

console.log(maxDepth(node3)); // expect 3
console.log(maxDepth(null)); // expect 0
console.log(maxDepth(new TreeNode(1))); // expect 1
