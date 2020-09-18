# sort()对列表排序，会自动按字母顺序对字符串从小到大排序，如果是数字，就会按数字顺序从小到大排序
# sort是在原地修改列表。说明会改变提供的元素列表，而不是创建一个新的有序列表。所以不能这样做，如
# print letters.sort(),这会得到None,必须使用下边的两步来完成。
letters = ['b', 'e', 'c', 'd', 'a']
print(letters)
letters.sort()
print(letters)
# reverse对列表逆序排序，有两种方法。一种方法是先按正常方式对列表排序，然后对这个有序列表完成
# 逆置。
letters.reverse()
print(letters)
# 另一种逆序排序的方法是sort（）增加一个参数，直接让它按降序排序（从大到小）
letters = ['b', 'e', 'c', 'd', 'a', 'f']
letters.sort(reverse=True)
print(letters)
#所有排序和逆置都会对原来的列表做出修改。这说明，原来的列表已经没有了。如果希望保留原来的顺序
#而对列表的副本进行排序，可以使用分片记法建立副本。如下：
original_list = ['Tom','James','Sarah','Fred']
new_list = original_list[:]
new_list.sort()
print(original_list)
print(new_list)
#另一种排序方法是sorted,这种方法可以得到一个列表的有序副本而不影响原列表的顺序。
original = [5,2,3,1,4]
newer = sorted(original)
print(original)
print(newer)
