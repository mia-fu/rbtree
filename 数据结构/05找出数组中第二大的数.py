# encoding:utf-8
class Soultion(object):
    """
    简陋排序 平均时间复杂度为O(NlogN)
    """

    def find_second_large_num1(self, num_list):
        tmp_list = sorted(num_list)
        print "第二大的数是：{0}".format(tmp_list[-2])

    """
    用第一大和第二大的数值存储交换 平均时间复杂度为O(N)
    """

    def find_second_large_num2(self, num_list):
        first_large_num = num_list[0]
        second_large_num = num_list[0]
        for i in range(len(num_list)):
            if num_list[i] > first_large_num:
                second_large_num = first_large_num
                first_large_num = num_list[i]
            elif num_list[i] > second_large_num:
                second_large_num = num_list[i]
        print "第二大的数是：{0}".format(second_large_num)


if __name__ == "__main__":
    s = Soultion()
    s.find_second_large_num1([1, 2, 3, 4, 5])
    s.find_second_large_num2(['a', 'b', 'c', 'd', 'e'])
