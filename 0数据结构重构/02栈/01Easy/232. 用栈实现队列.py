# encoding:utf-8
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 使用两个队列，一个输入队列，一个输出队列
        self.outstack = []
        self.instack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        # 进队列的时候，只要放在入栈里就可以了
        self.instack.append(x)



    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # 出的时候，先判断出栈中有没有元素
        if len(self.outstack) == 0:
            while len(self.instack):
        # 如果为空， 将入栈中的元素全部放到出栈中
                self.outstack.append(self.instack.pop())
        # 弹出一个
        return self.outstack.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.outstack) == 0:
        # 如果出栈为空，就将入栈的元素全都转移到出栈中
            while len(self.instack):
                self.outstack.append(self.instack.pop())
        # 弹出栈中的最后一个元素
        return self.outstack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.instack) == 0 and len(self.outstack) == 0



if __name__ == '__main__':
    myqueue = MyQueue()
    myqueue.push(1)
    myqueue.push(2)
    print myqueue.peek()
    print myqueue.pop()
    print myqueue.empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()