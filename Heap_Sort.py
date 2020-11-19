data = [82,24,11,47,19,91,2,32,85,7,16,36,99,52,41]
# ---------- 堆積排序法(Heap_Sort) ----------
#　http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php
# https://ithelp.ithome.com.tw/articles/10253199

# 採用最大堆積
# 將陣列轉換為 heap 資料結構（heapify）。
def Ｈeapify(data,n,i):
    largest = i     # root，將內部每個父節點視為樹根
    l = 2 * i + 1   # 左子樹
    r = 2 * i + 2   # 右子樹
    if l < n and data[l] > data[largest]:       # 當左子樹大於父節點(若最小堆積，則將data[l] > data[largest]改成data[l] < data[largest])
        largest = l
    if r < n and data[r] >  data[largest]:       # 當右子樹大於父節點(若最小堆積，則將data[l] > data[largest]改成data[r] < data[largest])
        largest = r
    '''
    左右子樹先比大小，大的子樹若大於父節點，則父節點位置為其位置
    if l < n and data[l] > data[r] and data[l] > data[largest]:       
        largest = data.index(data[l])
    if r < n and data[l] < data[r] and data[r] >  data[largest]:       
        largest = data.index(data[r])
    '''

    if largest != i:       # 當父節點位置不為原先的父節點位置，值互換
        temp = data[i]
        data[i] = data[largest]
        data[largest] = temp
        Ｈeapify(data, n, largest)


# 不斷置換 heap root 與最後一個元素來排序，並修正剩餘未排序資料使其符合 heap order。
def Ｈeap_Sort(data,n):
    last_parent = int(n/2-1)    # 最後一個父節點為n/2-1，取整數
    for i in range(last_parent,-1,-1):  # 所有的父節點(i)，範圍為0~n/2-1
        Ｈeapify(data,n,i)
    print("進行 Ｈeapify 後: ", data)

    # 將root和最後元素交換。並將最後一個元素(原root)取出，加入已排序陣列，未排序再進行一次Ｈeapify，重複以上動作，直到全部排序完成。
    for j in range(n-1,0,-1):

        # root和最後元素交換
        max_temp = data[0]
        data[0] = data[j]
        data[j] = max_temp
        # print("root 和 最後元素交換: ",data)

        # 未排序元素再次進行Ｈeapify
        Ｈeapify(data, j, 0)
        # print("交換後，進行heap order: ",data)
        # print("-------------------------")

if __name__ == '__main__':
    print("未進行 Ｈeap_Sort 前: ", data)
    n = len(data)
    Ｈeap_Sort(data,n)
    print("進行 Ｈeap_Sort 後: ", data)
