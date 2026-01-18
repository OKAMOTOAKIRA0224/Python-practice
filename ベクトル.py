#1.要素数が4つのベクトルを作成せよ。
import numpy as np
a=np.array([1,2,3,4])
print(a)

#2.2x2の行列を作成せよ。
b=np.array([[1,2,3],[4,5,6]])
print(b)

#3.(8,)(要素数８)のゼロベクトルおよび(4,3)のゼロ行列を作成せよ。
#また、(5,5)の単位行列も作成せよ。
c=np.zeros(8)
print(c)
print(c.shape)
d=np.zeros((4,3))
print(d)
e=np.eye(5)
print(e)

#4.次の計算をせよ
#A=1 5 2-1
#  4-3,7 6
#のときA+B,A-B,AB
A=np.array([[1,5],[4,-2]])
B=np.array([[2,-1],[7,6]])
print(A+B)
print(A-B)
print(np.dot(A,B))

#5.以下の行列から合計値、最大値、最小値、平均値、中央値、分散、標準偏差を取得せよ。
#  1 5 -2 
#A=4 0 -3
# -8 2  6
C=np.array([[1,5,-2],[4,0,-3],[-8,2,6]])
print(C.sum())
print(C.max())
print(C.min())
print(np.average(C))
print(np.median(C))
print(np.var(C))
print(np.std(C))

#6.以下の行列に逆行列がある場合その行列を求めよ
#A=1 5
#  4-2
D=([[1,5],[4,-2]])
d=np.linalg.det(D)
print(d)
d_inv=np.linalg.inv(D)
print(np.dot(D,d_inv))