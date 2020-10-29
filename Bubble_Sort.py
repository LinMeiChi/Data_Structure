data = ['A','S','O','R','T','I','N','G','E','X','A','M','P','L']

# ---------- 氣泡排序法 (Bubble_Sort) ----------
#https://emn178.pixnet.net/blog/post/93779892
def Bubble_Sort(n):
    for i in range(n-1,-1,-1):  # 未排序的最大值，會經每次比較，沉到最後面排序好(最後一位 -> 第一位)
        for j in range(0,i,1):  # 從未排序值中，由第一位開始，每次只和鄰居比較(第一位 -> 尚未排序的最後一位)
            if data[j] > data[j+1]:  # 若前值比後值大
                min = data[j+1]   # 則最小值為後值
                data[j+1] = data[j]   # 且後值與前值互換
                data[j] = min
    print("Bubble_Sort 後: ",data)


if __name__ == '__main__':
    print("未進行 Selection_Sort 前: ", data)
    n = len(data)  # key值在list中的index
    Bubble_Sort(n)