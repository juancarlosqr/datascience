#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 21:28:47 2018

@author: juancarlosqr
"""

import numpy as np

l1 = [100,200,300]
a = np.array(l1)
a
a[0]
a[1]
a[2]
a.dtype
# dtype('int64')
a.ndim # dimensions
# 1
a.size # length
# 3
a.shape # (len(1st-dim array), ..., len(n-th-dim array))
# (3,)

l2 = [[10,100],[20,200],[30,300]]
b = np.array(l2)
b
b[0]
b.ndim
# 2
b.size
# 6
b.shape
# (3, 2)

l3 = [[[10,100],[20,200],[30,300]], [[40,400],[50,500],[60,600]]]
c = np.array(l3)
c
c[0]
c[0][1]
c.ndim
# 3
c.size
# 12
c.shape
# (2, 3, 2)
c.itemsize # size in bytes
# 8

l4 = [[10,100,1000,10000], [20,200,2000,20000], [30,300, 3000,30000]]
d = np.array(l4)
d
d[0]
d.ndim
# 2
d.size
# 12
d.shape
# (3, 4)
d.itemsize # size in bytes
# 8
d.data
# <memory at 0x11d4ff2d0>

# with tuples

t1 = ((10,100),(20,200),(30,300),(40, 400))
e = np.array(t1)
e
e.dtype
e.dtype.name
e[0]
e.ndim
# 2
e.size
# 8
e.shape
# (4, 2)

l5 = [100,200,300]
f = np.array(l1, dtype=complex)
f
# array([ 100.+0.j,  200.+0.j,  300.+0.j])
f.dtype
# dtype('complex128')