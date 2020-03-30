# encoding:utf-8

"""
栈满压栈的异常类
"""


class StackEmptyException(Exception):
    pass


"""
栈空弹栈的异常类
"""


class StackFullException(Exception):
    pass


class Stack:
    """
    Stack based on array/list:
        |   4   |
        |   3   |
        |   2   |
        |   1   |
         -------
    """

    def __init__(self, max=0):
        self._array = []
        self._max = 0
        self.max = max


    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, m):
        m = int(m)
        if m < self.length:
            raise Exception('Resize stack failed, please pop some elements first.')
        self._max = m
        if self._max < 0:
            self._max = 0

    def init(self, iterable=()):
        if not iterable:
            return
        for i in iterable:
            self._array.append(i)

    def show(self):
        def _traversal(self):
            if not self._array:
                return [None]
            return self._array[::-1]

        print('\n'.join(map(lambda x: '|{:^7}|'.format(str(x)), _traversal(self))) + '\n ' + 7 * '-')

    @property
    def length(self):
        return len(self._array)

    @property
    def is_empty(self):
        return self._array == []

    @property
    def is_full(self):
        return bool(self._max and self.length == self._max)

    def push(self, item):
        if self.is_full:
            raise StackFullException('Error: trying to push element into a full stack!')
        self._array.append(item)

    def pop(self):
        if self.is_empty:
            raise StackEmptyException('Error: trying to pop element from an empty stack!')
        return self._array.pop()

    def top(self):
        return self._array[-1]

    def clear(self):
        # self._array = []
        while self._array:
            self.pop()


def test(stack):
    print('\nShow stack:')
    stack.show()

    print('\nInit linked list:')
    stack.init([1, 2, 3, 4, 5])
    stack.show()

    print('\nPush element to stack:')
    stack.push(6)
    stack.push(7)
    stack.push('like')
    stack.show()

    print('\nCheck top element:')
    print(stack.top())

    print('\nPop element from stack:')
    e = stack.pop()
    print('Element %s popped,' % e)
    stack.show()

    print('\nSet stack max size:')
    try:
        stack.max = 1
    except Exception as e:
        print(e)

    print('\nSet stack max size:')
    stack.max = 7
    print(stack.max)

    print('\nPush full stack:')
    try:
        stack.push(7)
    except StackFullException as e:
        print(e)

    print('\nClear stack:')
    stack.clear()
    stack.show()

    print('\nStack is empty:')
    print(stack.is_empty)

    print('\nPop empty stack:')
    try:
        stack.pop()
    except StackEmptyException as e:
        print(e)


if __name__ == '__main__':
    test(Stack())