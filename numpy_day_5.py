# -*- coding: utf-8 -*-
"""numpy day 5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L6v_xetROY2Tls-w36fWuocUgwXyyBOR
"""

import numpy as np

np1 = np.array([100,200,300])
np1

type(np1)

np2 = np.random.randint(10,20,(4,4))
np2

type(np2)

ary2 = np.random.randint(10,20,(4,4))
ary2

np2 + ary2

ary2 * np2

ary2- np2

m2 = np.matrix(ary2)
m2

ary2

m3 = np.matrix(np2)

type(m3)

# to create a matrix
mat1 = np.matrix("1,2,22;3,4,44;5,6,66")
mat2 = np.matrix("1,2;3,4")

mat2

#to find out the detemenant of a matrix
np.linalg.det(mat1)
####################################################

