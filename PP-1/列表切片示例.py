#列表切片
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[3:6])
print(numbers[0:1])
#如果要从列表末尾开始数，可使用负数索引
print(numbers[-3:-1])
#使用索引0的结果
print(numbers[-3:0])
#冒号后边没有数字，是指定索引到末尾的所有元素。因为这里是负数，所以是倒数。
print(numbers[-3:])