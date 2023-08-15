# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val = 0, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

queue = [(root, 0)]
values = []
maxLevel = 0
while len(queue) > 0:
    current, curLevel = queue.pop(0)
if curLevel > maxLevel:
    maxLevel = curLevel
if current != None:
    values.append((current.val, curLevel + 1))
queue.append((current.left, curLevel + 1))
queue.append((current.right, curLevel + 1))
            else:
values.append((0, curLevel + 1))

print(values)
length = len(values)


print(maxLevel)
output = 0
for i in range(length):
    if values[i][1] == maxLevel:
        output += values[i][0]

return output


























