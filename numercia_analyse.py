#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:12:06 2021

@author: xfh
"""

import numpy as np
#from numba import vectorize
import sympy as sy



def interpolation(data_x, data_fx, predict_x):
    '''
    拉格朗日内插法

    Parameters
    ----------
    data_x : numpy.array,一维
        数据点中x的序列
    data_fx : numpy.array,一维
        数据点中fx的序列
    predict_x : numpy.array,一维
        要预测的点的横坐标的序列

    Returns
    -------
    predict_y : array
        预测的序列

    '''
    predict_x = predict_x[:, np.newaxis, np.newaxis]
    data_x_jk = (data_x - data_x.T)
    bool_mat = np.eye(len(data_x), dtype = bool)
    data_x_jk[bool_mat] = 1
    data_x_xj = (data_x - predict_x) + np.zeros_like(data_x.T)
    #print(bool_mat)
    #print(np.zeros_like(predict_x) == 0)
    bool_mat = bool_mat * np.full(predict_x.shape, True, dtype = bool)
    #print(bool_mat)
    data_x_xj[bool_mat] = 1
    l = (data_x_xj / data_x_jk)
    #print(l.shape)
    l = l.prod(1)
    predict_y = (data_fx * l).sum(1)
    return predict_y

def solve_dic(fx, a, b, e = 1e-5):
    #二分法
    if fx(a) * fx(b) > 0:
        raise ValueError('[%f,%f]该区间两端点同号' % (a, b))
    c = (a + b) / 2
    if np.abs(a - b) < e:
        print(c)
        return c
    if fx(a) * fx(c) < 0:
        solve_dic(fx, a, c, e)
    elif fx(b) * fx(c) < 0:
        solve_dic(fx, b, c, e)
        
def solve_one_iteration(fx, x0, e = 1e-5):
    #单点迭代法
    #输入fx时求解方程fx = x
    if np.abs(fx(x0) - x0) < e:
        return x0
    l = [x0]
    while True:
        x_ = fx(l[-1])
        print(x_)
        if x_ in l:
            raise ValueError('迭代序列震荡')
        l.append(x_)
        if np.abs(fx(l[-1]) - l[-1]) < e:
            return l[-1]
        elif np.abs(l[0] - l[1]) < np.abs(l[-1] - l[-2]):
            raise ValueError('迭代序列不收敛')
            

def newton_iteration(fx, x, x0, e1, e2, N):
    #牛顿迭代法
    #fx为sympy表达式
    fx_ = fx.diff(x)
    for n in range(N + 1):
        result = fx.evalf(subs = {x : x0})
        result_ = fx_.evalf(subs = {x : x0})
        if np.abs(result) < e1:
            return x0
        elif np.abs(result_) < e2:
            raise ValueError('存在极点')
        x1 = x0 - result / result_
        tol = np.abs(x1 - x0)
        if tol < e1:
            return x1
        x0 = x1
    raise ValueError('抵达迭代次数上限')
    
    

# =============================================================================
# if __name__ == '__main__':
#     data_x = tuple(filter(None,input('data_x:').split(' ')))
#     data_fx = tuple(filter(None,input('data_x:').split(' ')))
#     x = tuple(filter(None,input('x:').split(' ')))
#     
#     data_x = np.array(tuple(map(eval,data_x)))[:,np.newaxis]
#     data_fx = np.array(tuple(map(eval,data_fx)))
#     x = np.array(tuple(map(eval, x)))
#     #print(x)
#     
#     y = interpolation(data_x, data_fx, x)
#     print(y)
# =============================================================================
    
if __name__ == '__main__':
    x = sy.Symbol('x')
    fx = sy.exp(-x) + sy.sin(x)
    result = newton_iteration(fx, x, 0.6, 1e-8, 1e-8, 100000)
    print(result)
