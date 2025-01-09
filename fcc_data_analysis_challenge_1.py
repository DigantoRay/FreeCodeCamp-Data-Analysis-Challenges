# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 21:40:55 2025

@author: sandh
"""

import numpy as np


def calculate(nums):
    if len(nums) != 9:
        raise ValueError('List must contain nine numbers.')
    arr = np.reshape(nums, (3, 3))
    parameters = ['mean',
                  'variance',
                  'standard deviation',
                  'max',
                  'min',
                  'sum'
                  ]
    stats = [[list(arr.mean(axis=0)), list(arr.mean(axis=1)), arr.mean()],
             [list(arr.var(axis=0)), list(arr.var(axis=1)), arr.var()],
             [list(arr.std(axis=0)), list(arr.std(axis=1)), arr.std()],
             [list(arr.max(axis=0)), list(arr.max(axis=1)), arr.max()],
             [list(arr.min(axis=0)), list(arr.min(axis=1)), arr.min()],
             [list(arr.sum(axis=0)), list(arr.sum(axis=1)), arr.sum()],
             ]
    calculations = {parameters[i]: stats[i] for i in range(6)}

    return calculations
