data = ['A','S','O','R','T','I','N','G','E','X','A','M','P','L']

# ---------- 插入排序法 (Insert_Sort) ----------
# https://emn178.pixnet.net/blog/post/93791164
def Insert_Sort(n):
    for i in range(1,n,1):  # 第一位視為已排序,(第二位 -> 最後一位)中
        temp = data[i]    # 取未排序第一位做為新的已排序值
        for j in range(i,0,-1):   # 已排序的範圍為 i -> 0(亦即比較範圍)，由後往前比較
            if data[j] < data[j-1]:   # 若新已排序值，比前面小
                data[j] = data[j-1]     # 則新值與比其大的值互換
                data[j-1] = temp
    print("Insert_Sort 後: ",data)


if __name__ == '__main__':
    print("未進行 Selection_Sort 前: ", data)
    n = len(data)  # key值在list中的index
    Insert_Sort(n)