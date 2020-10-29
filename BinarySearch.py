data = [2,5,6,9,11,14,16,18,34,33,37,40,45,48,50]
# ---------- 二分搜尋法(Binary_Search) ----------
def Binary_Search(key,L,U,count):
    if L <= U:
        M = int((L+U)/2)
        if key < data[M]: # 太大，調上限
            count += 1
            return Binary_Search(key,L,M-1,count)
        elif key > data[M]: # 太小，調下限
            count += 1
            return Binary_Search(key, M+1,U,count)
        else:
            count += 1
            print("找到 Binary_Search 的key: ",data[M])
            print("共需要比較" ,count, "次")
            return M
    else:
        return -1 # 表示找不到




if __name__ == '__main__':
    key = 37
    n = data.index(key) # key值在list中的index
    U = len(data) # index上限
    L = 0 # index下限
    count = 0 # 比較次數
    Binary_Search(key, L, U,count)