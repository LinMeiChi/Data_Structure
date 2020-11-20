import math
import random

data = [26,5,77,1,61,11,59,15,48,19]
# ---------- 合併排序法(Merge_Sort) ----------
# 採用遞迴合併排序法:先進行兩兩切割，再依據切割過程進行反向合併。
# 先對陣列進行切割，直到切割到最小單元(每個陣列只剩下一個元素)。
#ttps://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e

# 方法一:
def segmentation(data):
    n = len(data)

    # 如果陣列長度小於等於1，就直接回傳。
    if 1 >= len(data):
        return data

    # 否則，進行下面的切割動作
    left_array = data[0:n // 2]
    right_array = data[n // 2:]
    '''
            * data[0:n/2]遇到問題:
                TypeError: slice indices must be integers or None or have an __index__ method
            * 解決方法:
                除法(/)會自動產生的型別是浮點型，因此出現上述錯誤，故將 / 改成 // 。
            '''
    # 反覆切割，直到陣列變成最小單元。
    left = segmentation(left_array)
    right = segmentation(right_array)

    # 當無法再分割，進行合併
    return Merge_Sort(left, right)

def Merge_Sort(left, right):

    # 當左(右)陣列為空值時，直接回傳右(左)陣列。
    if len(left) == 0:
        return right
    elif len(right) == 0:
        return left

    # 對左右陣列的第一個值做比較，若左1值較小，則將其值提出，並重複進行比較、合併。反之，為反向。
    elif left[0] < right[0]:
        return [left[0]] + Merge_Sort(left[1:], right)
    else:
        return [right[0]] + Merge_Sort(left, right[1:])

if __name__ == '__main__':
    print("未進行 Merge_Sort 前: ", data)
    merge_sort = segmentation(data)
    print("進行 Merge_Sort 後: ", merge_sort)



# # 方法二:
# def merge_sort(left, right):
#     sort_array = []     # 建立已排序的新陣列。
#     while left and right:
#         if left[0] < right[0]:
#             sort_array.append(left.pop(0))      # pop() 函數用於移除列表中的一個元素（默認最後一個元素），並且返回該元素的值。
#         else:
#             sort_array.append(right.pop(0))
#     sort_array = sort_array + left + right
#     return sort_array
#
# def segmentation(data):
#     if len(data) <= 1:
#         return data
#     mid = len(data)//2
#     left = segmentation(data[:mid])
#     right = segmentation(data[mid:])
#     return merge_sort(left,right)
# if __name__ == '__main__':
#     print("未進行 Merge_Sort 前: ", data)
#     merge_sort = segmentation(data)
#     print("進行 Merge_Sort 後: ", merge_sort)
