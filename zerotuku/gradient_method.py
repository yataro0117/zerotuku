import numpy as np
#勾配
def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x) #xと同じ形状の配列でその要素がすべて0の配列を生成する

    for idx in range(x.size):
        tmp_val = x[idx]
        #f(x+h)の計算
        x[idx] = tmp_val + h
        fxh1 = f(x)

        #f(x-h)の計算
        x[idx] = tmp_val - h
        fxh2= f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val

    return grad




#勾配降下法
#ｆ：最適化したい関数　init_x:初期値　lr:learning rate
def gradient_descent(f, init_x,lr=0.01,step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr*grad

    return x

#example f(x0,x1) = x0^2 + x1^2
def function_2(x):
    return x[0]**2 +x[1]**2

init_x = np.array([-3.0, .0])
print(gradient_descent(function_2, init_x=init_x, lr=0.1, step_num=100))