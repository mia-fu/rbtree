# encoding:utf-8


class Rectangle():
    width = 1
    length = 1

    def setRec(self):
        print("请输入矩形的长和宽")
        self.length = float(raw_input('长为：'))
        self.width = float(raw_input('宽为：'))

    def getArea(self, length, width):
        area = self.length * self.width

        return area


rec = Rectangle()
rec.setRec()
print "矩形的面积为：" + str(rec.getArea(rec.length, rec.width))


