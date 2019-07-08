class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.queue1!=[]:
            self.queue1.append(x)
        else:
            self.queue2.append(x)
            
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.queue1!=[]:
            while len(self.queue1)!=1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)
        else:
            while len(self.queue2)!=1:
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop(0)
        
            
        
        

    def top(self) -> int:
        """
        Get the top element.
        """
        x = self.pop()
        self.push(x)
        return x
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not (self.queue1 or self.queue2)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
