# encoding:utf-8
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 需要一个数据值栈和一个最小值栈
        self.dataStack = []
        self.minStack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # 将数据压入数据栈中，
        self.dataStack.append(x)
        # 判断如果最小值栈中没有数据，将数据压入最小值栈中
        if len(self.minStack) == 0:
            self.minStack.append(x)
        else:
            if x > self.minStack[-1]:
                self.minStack.append(self.minStack[-1])
            else:
                self.minStack.append(x)
        # 否则判断 x是否比最小值栈中的栈顶元素小，如果小，压入最小值占中


    def pop(self):
        """
        :rtype: None
        """
        # 将数据栈中的元素， 与最小值栈中的栈顶元素pop出来，并返回
        self.dataStack.pop()
        return self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.dataStack[-1]

        # 返回数据栈中的栈顶元素


    def getMin(self):
        """
        :rtype: int
        """
        # 返回最小值栈中的栈顶元素
        return self.minStack[-1]


if __name__ == '__main__':
    myqueue = MinStack()
    myqueue.push(-2)
    myqueue.push(0)
    myqueue.push(-3)
    print myqueue.getMin()
    print myqueue.pop()
    print myqueue.top()
    print myqueue.getMin()
