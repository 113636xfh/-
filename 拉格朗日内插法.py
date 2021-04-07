#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:12:06 2021

@author: xfh
"""

import numpy as np
#from numba import vectorize

def interpolation(data_x, data_fx, predict_x):
    predict_x = predict_x[:, np.newaxis, np.newaxis]
    data_x_jk = (data_x - data_x.T)
    bool_mat = data_x_jk == 0
    data_x_jk[bool_mat] = 1
    data_x_xj = (data_x - predict_x) + np.zeros_like(data_x.T)
    #print(bool_mat)
    #print(np.zeros_like(predict_x) == 0)
    bool_mat = bool_mat * (np.zeros_like(predict_x) == 0)
    #print(bool_mat)
    data_x_xj[bool_mat] = 1
    l = (data_x_xj / data_x_jk)
    #print(l.shape)
    l = l.prod(1)
    predict_y = (data_fx * l).sum(1)
    return predict_y

if __name__ == '__main__':
    data_x = tuple(filter(None,input('data_x:').split(' ')))
    data_fx = tuple(filter(None,input('data_x:').split(' ')))
    x = tuple(filter(None,input('x:').split(' ')))
    
    data_x = np.array(tuple(map(eval,data_x)))[:,np.newaxis]
    data_fx = np.array(tuple(map(eval,data_fx)))
    x = np.array(tuple(map(eval, x)))
    print(x)
    y = interpolation(data_x, data_fx, x)
    print(y)

