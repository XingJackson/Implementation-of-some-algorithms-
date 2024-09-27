import random

from param import output


# get the matrix size
def get_size(lst):
    if isinstance(lst, list) and lst:  # 检查是否为非空列表
        return [len(lst)] + get_size(lst[0])  # 递归获取下一级的尺寸
    return []


# basic info
batch= 1
h = 56
w = 56
in_channel = 3
out_channel = 64
kernel_size = 3
test_stride = 1
padding = 0

# Initialize a random matrix
test_input = [[[random.randint(0, 10) for _ in range(3)] for _ in range(56)] for _ in range(56)]
kernel = [values for values in range(kernel_size ** 2)]
im2col = []
print("The Initial matrix size:", get_size(test_input))

# change the layout
for i in range(in_channel):  # every channel of input
    layer = []
    for j in range(h - 2):
        for k in range(w - 2):
            layer.append([test_input[j][k][i], test_input[j][k + 1][i], test_input[j][k + 2][i],
                          test_input[j + 1][k][i], test_input[j + 1][k + 1][i], test_input[j + 1][k + 2][i],
                          test_input[j + 2][k][i], test_input[j + 2][k + 1][i], test_input[j + 2][k + 2][i]])
    im2col.append(layer)
print("After the translation of im2col:", get_size(im2col))

print("After the translation of im2col in one channel:", get_size(im2col[0]))

# cal the result size
new_h = h - kernel_size + 1
new_w = w - kernel_size + 1
kernel = [[values for values in range(kernel_size ** 2)] for _ in range(out_channel)]

# achieve the col
res = []
for i in range(len(im2col[0])):
    temp = []
    for j in range(len(kernel)):
        tempsum = 0
        for k in range(len(im2col)):
            tempsum = tempsum + sum(a * b for a, b in zip(im2col[k][i], kernel[j]))
        temp.append(tempsum)
    res.append(temp)

# get the output
output = []
index = 0
for i in range(new_h):
    temp = []
    for j in range(new_w):
        temp.append(res[index])
    output.append(temp)

print("The output result size:", get_size(output))
