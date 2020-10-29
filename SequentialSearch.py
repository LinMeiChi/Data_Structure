data = [2,5,6,9,11,14,16,18,34,33,37,40,45,48,50]

# ---------- 循序搜尋演算法 (Sequential_search) ----------
def Sequential_Search(n,key,U):
    for i in range(0,U,1): # range(起始值,結束值,遞增減值)

        # 以key去找
        if data[i] == key:
            print("find the key: ", data[i])
        else:
            i += 1 # Python不支援 i++

        # # 以index去找
        # if i != n:
        #     continue
        # else:
        #     print("找到Sequential_Search的key: ",data[i])


if __name__ == '__main__':
    key = 37
    n =  data.index(key) # key值在list中的index
    U = len(data) # index上限
    Sequential_Search(n,key,U)





