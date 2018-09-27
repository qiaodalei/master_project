import treePlotter
import trees
import matplotlib.pyplot as plt
from math import log
import operator

fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
print(lenses)
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = trees.createTree(lenses, lensesLabels)
print(lensesTree)
treePlotter.createPlot(lensesTree)