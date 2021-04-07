#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:12:06 2021

@author: xfh
"""

import numpy as np

def interpolation(data_x, data_fx):
    data_x_jk = (data_x - data_x.T)
    bool_mat = data_x_jk == 0
    data_x_jk[bool_mat] = 1
    data_x_xj = (data_x - x) + np.zeros_like(data_x.T)
    data_x_xj[bool_mat] = 1
    l = (data_x_xj / data_x_jk).prod(0)
    y = (data_fx * l).sum()
    return y

if __name__ == '__main__':
    data_x = tuple(filter(None,input('data_x:').split(' ')))
    data_fx = tuple(filter(None,input('data_x:').split(' ')))
    x = eval(input('x:'))
    
    data_x = np.array(tuple(map(eval,data_x)))[:,np.newaxis]
    data_fx = np.array(tuple(map(eval,data_fx)))
    y = interpolation(data_x, data_fx)
    print(y)

