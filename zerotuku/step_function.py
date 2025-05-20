#simplest step kannsuu
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0
print(step_function(2))

#行列の入力ができるように拡張
import numpy as np
x = np.array([-1.0, 1.0, 2.0])
print(x)
y = x > 0   #ブーリアンの配列
print(y)

y = y.astype(int)  #astype(型)で希望する型に！
print(y)

#グラフ化
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=int) #最初からnumpy配列の型を指定

x = np.arange(-5.0, 5.0, 0.1) #[-5.0,-4.9,・・・,4.9]を生成
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
