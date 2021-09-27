from collections import Counter, deque
from typing import Dict
import numpy as np


class Node:
    left = None
    right = None
    label = None
    nmin = 0
    minleaf = 0
    nfeat = 0

    x: np.array = []
    X: np.array = []
    y: np.array = []

def tree_grow(X: np.array, y: np.array, nmin: int = 2, minleaf: int = 1, nfeat: int = None):
    return Node(x,y,nmin,minleaf,nfeat)

def bestsplit(x: np.array, y: np.array):
    unique_sorted = np.sort(np.unique(x))
    splitpoints = (unique_sorted[0:len(unique_sorted) - 1] + unique_sorted[1:len(unique_sorted)]) / 2

    best_split = 0
    impurity = 2

    for splitpoint in splitpoints:
        right = y[x <= splitpoint]
        left = y[x > splitpoint]

        quality_of_split = impurity(left) + impurity(right)
        if impurity > quality_of_split:
            impurity = quality_of_split
            best_split = splitpoint
        return best_split

def impurity(x):
    unique, counts = np.unique(x, return_counts=True)
    total = np.sum(counts)
    if counts.size ==1 or counts[0:1] == 0:
        return 0
    else:
        gini_impurity = (counts[0]/total) * (counts[1]/total)
        return gini_impurity


