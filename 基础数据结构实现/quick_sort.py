# -*- coding:utf-8 -*-

# 快速排序实现

def quick_sort_easy(arr):
    if not arr:
        return []
    mid = len(arr) >> 1
    left = [i for i in arr if arr[i] < arr[mid]]
    equal = [i for i in arr if arr[i] == arr[mid]]
    right = [i for i in arr if arr[i] > arr[mid]]
    return quick_sort(left) + equal + quick_sort(right)


# 比较容易理解的交换
def quick_sort_by_shift_left(arr, low, high):
    if low >= high:
        return
    i = low
    for j in range(low, high):
        if arr[j] <= arr[high]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[i], arr[high] = arr[high], arr[i]
    quick_sort_by_shift_left(arr, low, i - 1)
    quick_sort(arr, i + 1, high)


def quick_sort(item, first, last):
    """
    快速排序
    最优时间复杂度：O(nlogn)
    最坏时间复杂度：O(n^2)
    不稳定排序算法
    :param item:
    :param first:起始值索引
    :param last:最后值索引
    :return:
    每次挑选一个元素，放在合适的位置，比它大的放右边，比他小的放左边
    """
    if first < last:
        mid_value = item[first]
        low = first
        high = last
        while low < high:
            while (low < high) and item[high] >= mid_value:
                high -= 1
            item[low] = item[high]

            while (low < high) and item[low] < mid_value:
                low += 1
            item[high] = item[low]
        item[low] = mid_value
        quick_sort(item, first, low - 1)
        quick_sort(item, low + 1, last)
    return item


if __name__ == '__main__':
    li = [0, -89, 8, 2, 99, 53]
    print(li)
    print(quick_sort(li, 0, len(li) - 1))
