class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_list = []
        self.queue_list = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.queue_list!=[]:
            self.stack_list.append(self.queue_list.pop())
        self.stack_list.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.stack_list!=[]:
            self.queue_list.append(self.stack_list.pop())
        x = self.queue_list.pop()
        return x
        
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.stack_list!=[]:
            self.queue_list.append(self.stack_list.pop())
        x = self.queue_list[-1]
        return x
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack_list == [] and self.queue_list == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
