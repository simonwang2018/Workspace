age = 23
if age >= 18:
    print('your age is',age)
    print('adult')
#根据python的缩进规则，如果if语句判断为true,就把缩进的两行print语句执行了，否则，什么也不做。
#也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了。
else:
    print('your age is',age)
    print('teenager') 
#上面的判断很粗略，完全可以用elif做更细致的判断。
age = 8
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
#elif是else if的缩写，完全可以有多个elif,所以if语句的完整形式就是。
'''if <条件判断1>：
      <执行1>
   elif <条件判断2>:
        <执行2>
   elif <条件判断3>:
        <执行3>
   else:
        <执行4> '''
#if语句执行是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就会忽略掉剩下的elif和else。
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
