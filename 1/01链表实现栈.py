# encoding:utf-8
# Definition for singly-linked list.
class LinkedStacked:
    class _Node:
        __slot__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # 设置栈顶
    def __init__(self):
        self._head = None
        self._size = 0

    # 元素压栈
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1






if __name__ == "__main__":
    ls = LinkedStacked()
    ls.push(1)
    ls.push(2)
    ls.push(3)

    print ls._head._element
    print ls._head._next._element