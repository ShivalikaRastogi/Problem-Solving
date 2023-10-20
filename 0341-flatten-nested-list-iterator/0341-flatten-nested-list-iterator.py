# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        # Add the nestedList to the stack in reverse order
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])        
    
    def next(self) -> int:
        return self.stack.pop().getInteger()        
    
    def hasNext(self) -> bool:
        # Flatten the list by popping elements from the stack until we find an integer
        while self.stack:
            current = self.stack[-1]
            if current.isInteger():
                return True

            # If it's a list, pop it and push its elements in reverse order
            self.stack.pop()
            nested_list = current.getList()
            for i in range(len(nested_list) - 1, -1, -1):
                self.stack.append(nested_list[i])

        return False 

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())