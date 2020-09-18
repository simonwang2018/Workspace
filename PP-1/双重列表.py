joemarks = [55,63,77,81]
tommarks = [65,61,67,72]
bethmarks = [97,95,92,88]
classmarks = [joemarks,tommarks,bethmarks]
print(classmarks)
#还可以直接创建classmarks，而不需要先创建joemarks,tommarks和bethmarks。
classmarks = [[55,63,77,81],[65,61,67,72],[97,95,92,88]]
print(classmarks)
#classmarks有3个元素，每个元素分别对应一个学生，所以可以用In来循环处理。
for studentmarks in classmarks:
    print(studentmarks)
#想得到某个元素中其中的一个值，可以使用分片
print(classmarks[0][2])#这里得到的是第一个元素列表中的第3个元素。