data = [82,24,11,47,19,91,2,32,85,7,16,36,99,52,41]
# ---------- 快速排序法(Quick_Sort) ----------
# https://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html

# 方法一:
def Quick_Sort(data,left,right):
    if left < right:
        i = left+1       # 左指標
        j = right       # 右指標
        pivot = data[left]    # 將index=0的值視為pivot。
        while(1):   # 永真迴圈，為無止境迴圈，無假的可能。
            while (i <= right and data[i] < pivot):     # 當符合條件(i在0~右指標內，且此數比pivot小)則i+1。此方法可以取出第一個比pivot大的值。
                i += 1
            while (j >= left and data[j] > pivot):     # 當符合條件(j在n元素-1~左指標內，且此數比pivot大)則j-1。此方法可以取出第一個比pivot小的值。
                j -= 1
            if i < j:       # 若此時，左指標小於右指標，則i值與j值互換。
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
            else:       # 否則，跳出迴圈。將pivot和j值互換。並將j值當作分割點，分成左陣列和右陣列。
                break
        data[left] = data[j]
        data[j] = pivot
        Quick_Sort(data,left,j-1)       # 新左陣列
        Quick_Sort(data,j+1,right)      # 新右陣列


if __name__ == '__main__':
    print("未進行 Quick_Sort 前: ",data)
    # 陣列的範圍在 left(左:0) ~ right(右:n元素-1)
    '''
    陣列和串列差異:
    * 陣列(Array): 包含的所有元素類型都必須相同。
    * 串列(List): 包含的所有元素類型可以不相同。
    '''
    left = 0
    right = len(data)-1
    Quick_Sort(data,left,right)
    print("Quick_Sort 後: ",data)



# # 方法二:
# def quicksort(data, left, right): # 輸入資料，和從兩邊開始的位置
#     if left >= right :            # 如果左邊大於右邊，就跳出function(return空值 = return None)
#         return
#
#     i = left                      # 左邊的代理人
#     j = right                     # 右邊的代理人
#     key = data[left]                 # 基準點
#
#     while i < j:
#         while data[j] > key and i < j:   # 從右邊開始找，找比基準點小的值
#             j -= 1
#         while data[i] <= key and i < j:  # 從左邊開始找，找比基準點大的值
#             i += 1
#         if i < j:                        # 當左右代理人沒有相遇時，互換值
#             data[i], data[j] = data[j], data[i]
#
#     # 將基準點歸換至代理人相遇點
#     data[left] = data[i]
#     data[i] = key
#
#     quicksort(data, left, i-1)   # 繼續處理較小部分的子循環
#     quicksort(data, i+1, right)  # 繼續處理較大部分的子循環
#
# quicksort(data, 0, len(data)-1)
# print(data)



