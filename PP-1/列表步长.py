#列表步长
numbers = [1,2,3,4,5,6,7,8,9,10]
#执行切片操作时，通常省略另一个参数，即步长。在普通切片中，步长为1.这意味着从一个元素移到下一个元素，
#因此切片包含起点和终点之间的所有元素。
print(numbers[0:10:1])
#如果指定的步长大于1，将跳过一些元素。例如，步长为2时，将从起点和终点之间每隔一个元素提取一个元素。
print(numbers[0:10:2])
#例如，要从序列中每隔3个元素提取1个，只需提供步长4即可。
print(numbers[0:10:4])
#当然，步长不能为0，否则无法向前移动，但可以为负数，即从右向左提取元素。
print(numbers[8:3:-1])
print(numbers[10:0:-2])
print(numbers[::-2])
print(numbers[5::-2])
print(numbers[:5:-2])