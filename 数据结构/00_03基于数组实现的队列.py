# encoding:utf-8
class Node(object):
    def __init__(self, value):
        self.next = None
        self.val = value

class Queue(object):
    def __init__(self):
        self.first = None # first删除端
        self.last = None # last插入端

    def enqueue(self, n):
        n = Node(n)
        if(self.first == None):
            self.first =n
            self.last = n
        else:
            self.last.next = n
            self.last = n

    def dequeue(self):
        if(self.first == None):
            return None
        else:
            reval = self.first.val
            self.first = self.first.next
        return reval

    def allquit(self):
        alist = []
        while(self.first != None):
            temp = self.first.val
            self.first = self.first.next
            alist.append(temp)
        return alist

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    q.dequeue()
    print (q.allquit())
