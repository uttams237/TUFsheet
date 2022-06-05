from os import *
from sys import *
from collections import *
from math import *
from typing import List

def setZeros(mat: List[List[int]]) -> None:
    row=set()
    col=set()
    m,n=len(mat),len(mat[0])
    
    for i in range(m):
        for j in range(n):
            if mat[i][j]==0:
                row.add(i)
                col.add(j)
#     print(row)
#     print(col)
    for i in range(m):
        for j in range(n):
            if i in row or j in col:
                mat[i][j]=0