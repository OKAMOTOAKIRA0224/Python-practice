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

#
#