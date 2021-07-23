# 插入排序


def insert_sort(item):
    """
    插入排序实现
    最优时间复杂度：O(n)
    最坏时间复杂度：O(n^2)
    稳定排序算法
    :param item:
    :return:
    """
    n = len(item)
    # 遍历每一个元素
    for j in range(1, n):
        i = j
        # 把当前遍历到的元素插入到已经排好序的列表中
        while i > 0:
            if item[i] < item[i-1]:
                item[i], item[i-1] = item[i-1], item[i]
                i -= 1
            else:
                break
    return item


if __name__ == '__main__':
    li = [0, -89, 8, 2, 99, 53]
    print(li)
    print(insert_sort(li))













