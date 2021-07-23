# 二分法查找
def binary_search(item, key):
    """
    二分法递归查找
    最优时间复杂度：O(1)
    最坏时间复杂度：O(logn)
    :param item:
    :param key:
    :return:
    """
    n = len(item)
    if n > 0:
        mid = n // 2
        if item[mid] == key:
            return True
        elif key < item[mid]:
            return binary_search(item[:mid], key)
        else:
            return binary_search(item[mid+1:], key)
    return False


def binary_search1(item, key):
    """
    非递归实现
    :param item:
    :param key:
    :return:
    """
    n = len(item)
    start = 0
    end = n - 1
    while start <= end:
        #防止溢出
        mid = start + (end-start) // 2
        if item[mid] == key:
            return item[mid]
        elif item[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return False


if __name__ == '__main__':
    li = [-89, 0, 2, 8, 53, 99]
    print(binary_search1(li, 2))
    print(binary_search1(li, 3))