import numpy as np
#二乗和誤差
def sum_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

#2を正解とする（教師データ）
t =[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

#２の確率が最も高い場合(ニューラルネットワークの出力)
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.1]
print(sum_squared_error(np.array(y), np.array(t)))

#７の確立が最も高い場合
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print(sum_squared_error(np.array(y), np.array(t)))





#交差エントロピー誤差
def cross_entropy_error(y, t):
    delta =1e-7
    return -np.sum(t * np.log(y +delta))
#2を正解とする（教師データ）
t =[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

#２の確率が最も高い場合(ニューラルネットワークの出力)
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.1]
print(cross_entropy_error(np.array(y), np.array(t)))
#７の確立が最も高い場合
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print(cross_entropy_error(np.array(y), np.array(t)))