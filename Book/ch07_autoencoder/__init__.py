import numpy as np

print(np.where([[0, 1], [1, 0]]))
print(np.where([[True, False], [True, True]],
               [[1, 2], [3, 4]],
               [[9, 8], [7, 6]]))

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])  # 两个数值数组
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])  # 一个布尔数组
result = np.where(cond, xarr, yarr)  # 三元表达式

print(result)
