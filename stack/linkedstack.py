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


class Node:
    def __init__(self, val=None, next=None):
        self.value = val
        self.next = next

    def __str__(self):
        return str(self.value)


class Stack:
    """
    Stack based on linked list:
        | item3 |
        |   |   |
        |   V   |
        | item2 |
        |   |   |
        |   V   |
        | item1 |
         -------
    """
    # 定义栈顶元素和栈的大小
    def __init__(self, max=0):
        self._top = None
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
        self._top = Node(iterable[0])
        for i in iterable[1:]:
            node = self._top
            self._top = Node(i)
            self._top.next = node

    def show(self):
        def _traversal(self):
            node = self._top
            while node and node.next:
                yield node
                node = node.next
            yield node

        print('\n'.join(map(lambda x: '|{:^7}|'.format(str(x)), _traversal(self))) + '\n ' + 7 * '-')

    @property
    def length(self):
        if self._top is None:
            return 0
        node = self._top
        i = 1
        while node.next:
            node = node.next
            i += 1
        return i

    @property
    def is_empty(self):
        return self._top is None

    @property
    def is_full(self):
        return bool(self._max and self.length == self._max)

    def push(self, item):
        if self.is_full:
            raise StackFullException('Error: trying to push element into a full stack!')
        if not self._top:
            self._top = Node(item)
            return
        node = self._top
        self._top = Node(item)
        self._top.next = node

    def pop(self):
        if self.is_empty:
            raise StackEmptyException('Error: trying to pop element from an empty stack!')
        node = self._top
        self._top = self._top.next
        return node.value

    def top(self):
        return self._top.value if self._top else self._top

    def clear(self):
        while self._top:
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