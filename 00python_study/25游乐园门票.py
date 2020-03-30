# encoding:utf-8


class Ticket:
    def __init__(self, weekend=False, child=False):
        self.price = 100
        if weekend:
            self.increase = 1.2
        else:
            self.increase = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def calPrice(self, num):
        return self.price * self.increase * self.discount * num


adult = Ticket()
chid = Ticket(child=True)
print("2个大人+1个小孩平日的票价为：%.2f" % (adult.calPrice(2) + chid.calPrice(1)))


adult = Ticket(weekend=True)
chid = Ticket(weekend=True, child=True)
print("2个大人+1个小孩周末的票价为：%.2f" % (adult.calPrice(2) + chid.calPrice(1)))

