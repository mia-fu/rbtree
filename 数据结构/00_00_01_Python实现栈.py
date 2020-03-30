# encoding:utf-8
class Node(object):
    def __init__(self, value):
        self.next = None
        self.val = value

class Stack(object):
    def __init__(self):
        self.top = None

    def push(self,n):
        n = Node(n)
        if(self.top == None):
            self.top = n
        else:
            n.next = self.top
            self.top = n

    def pop(self):
        if(self.top == None):
            return None
        else:
            temp = self.top.val
            self.top = self.top.next
        return temp

    def allquit(self):
        alist = []
        while(self.top != None):
            temp = self.top.val
            self.top = self.top.next
            alist.append(temp)
        print alist

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(5)
    s.pop()
    s.allquit()