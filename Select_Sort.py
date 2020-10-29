data = ['A','S','O','R','T','I','N','G','E','X','A','M','P','L']

# ---------- 選擇排序法 (Selection_Sort) ----------
# https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E5%85%A5%E9%96%80-%E9%81%B8%E6%93%87%E6%8E%92%E5%BA%8F%E8%88%87%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F%E6%B3%95-23d4bc7085ff
def Selection_Sort(n):
    for i in range(0,n-1,1):    # 從未排序的值開始(第一位 -> 倒數第二位，因為最後一位會在排序過程中，自動排好)
        min = data[i]   # 將已排序的右邊第一位(即未排序的第一個)，作為最小值
        for j in range(i+1,n,1):  # 將最小值與每一個未排序的值做比較( i+1 -> 最後一位)
            if min > data[j]:   # 若最小值較大
                min = data[j]   # 則最小值index j 的值取代
                data[j] = data[i]   # 且 index j 和 index i 的值互換
                data[i] = min
            else:
                min = min   # 若無值比最小值小，則最小值依然是最小值
    print("Selection_Sort 後: ",data)


if __name__ == '__main__':
    print("未進行 Selection_Sort 前: ", data)
    n = len(data)  # key值在list中的index
    Selection_Sort(n)
