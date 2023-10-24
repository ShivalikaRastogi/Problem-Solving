class Solution:
    def largestValues(self, root):
        maxLevelVal = []
        if root is None:
            return maxLevelVal
        levelQueue = []
        levelQueue.append(root)
        while levelQueue:
            sz = len(levelQueue)
            maxValNode = float('-inf')
            while sz > 0:
                currNode = levelQueue.pop(0)
                maxValNode = max(currNode.val, maxValNode)
                if currNode.left:
                    levelQueue.append(currNode.left)
                if currNode.right:
                    levelQueue.append(currNode.right)
                sz -= 1
            maxLevelVal.append(maxValNode)
        return maxLevelVal