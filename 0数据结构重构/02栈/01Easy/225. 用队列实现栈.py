# encoding:utf-8
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 使用两个队列，一个只进，一个只出
        self.inqueue = list()
        self.outqueue = list()
        self.i = 0
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        # 入栈的时候，只要往入队列里面放即可
        self.inqueue.insert(0, x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        # 出栈的时候，要先看出队列里面有没有
        if len(self.outqueue) == 0:
            while len(self.inqueue):
                self.outqueue.append(self.inqueue.pop())
        # 如果没有，要讲入队列中的元素放到出队列中
        return self.outqueue.pop()
        # 如果有，就弹出队列头即可


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        # # 出栈的时候，要先看出队列里面有没有
        while len(self.inqueue):
            self.outqueue.append(self.inqueue.pop())
        # 如果没有，要讲入队列中的元素放到出队列中
        return self.outqueue[-1]
        # 如果有，就返回队列头即可


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.inqueue) == 0 and len(self.outqueue) == 0

if __name__ == '__main__':
    mystack = MyStack()
    mystack.push(1)
    mystack.push(2)
    print mystack.top()
    mystack.push(3)
    print mystack.top()
    print mystack.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()