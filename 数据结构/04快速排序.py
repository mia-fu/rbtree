# encoding:utf-8

"""
快速排序， a表示数组， n表示数组⼤⼩
"""


# 快速排序
def quick_sorted(my_list, start, end):
    # 建立终止条件
    if start >= end:
        return

    # x为左边向右移动的游标
    # y为右边向右移动的游标
    i, j = start, end

    # 建立基准元素
    key = my_list[start]

    while i < j:

        # 当x<y,并且对应的元素都大于基准元素，游标向左移动
        while i < j and my_list[j] >= key:
            j = j - 1

        # 如果小于基准元素，则将值赋给x游标对应的元素
        my_list[i] = my_list[j]

        # 当x<y,并且对应的元素都小于基准元素，游标向右移动
        while i < j and my_list[i] <= key:
            i = i + 1

        # 如果大于基准元素，则将值赋给y游标对应的元素
        my_list[j] = my_list[i]

    # 当循环结束之后，x=y，则将基准元素赋值给x游标对应的元素
    my_list[i] = key

    # 此时序列被分成了前后两部分，利用递归调用继续排序
    # 前半部分序列进行递归
    quick_sorted(my_list, start, i - 1)

    # 后半部分序列进行递归
    quick_sorted(my_list, i + 1, end)
    return my_list

# 归并排序


if __name__ == '__main__':
    my_list = [45, 62, 23, 12, 54, 78, 96, 31]
    quick_sorted(my_list, 0, len(my_list) - 1)
    print(my_list)
