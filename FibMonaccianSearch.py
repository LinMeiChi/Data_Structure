# ---------- 費氏搜尋法(Fibonacci_Search) ----------
# 公式: Fib(n) = Fib(n-1) + Fib(n-2)
import pandas as pd
def Fib(n):
   if n == 0:
       return 0
   if n == 1:
       return 1
   else:
        return Fib(n-1) + Fib(n-2)

# ---------- 輸出F(n)所經過步驟的值 ----------
def step(n):
    n_list = []
    fib_list = []
    for i in range(0, n + 1, 1):
        n_list.append(i)
        fib_list.append(Fib(i))

        # ----- 以dataframe格式輸出 -----
        #方法一:
        frame = {"F(n)": fib_list}
        # Fin_frame = pd.DataFrame(frame,columns=n_list).T

        # 方法二:
        Fin_frame = pd.DataFrame([fib_list],index=['F(n)'],columns=n_list)
        print(" \n------ 當 n=%d 時，所有步驟的值為: -----\n"%i,Fin_frame)

if __name__ == '__main__':
    n = int(input("請輸入要搜尋的位置，只能輸入整數: "))
    Fib(n)
    print('Fib(%d) = '%n,Fib(n))
    step(n)



