set1 = {} #this is dict
set2 = {1,2,3,4,5} #this is set ，因为没有映射关系
#集合内的元素具有唯一性，绝对不就可以有相同的对象
set2 = {1,3,3,4,546,32,3,2,1,3}
print(set2) #集合是无序的，没有index

#使用函数创建集合
set1 = set([12,3,423,6,32,5,5,32,2])
print(set1)

#应用： 去掉列表中重复的元素
set2 = list(set([2,3,4,5,2,6,7,5,3,1]))
print(set2)

set2.append(8)
print(set2)
set2.remove(2)
print(set2)

#不可改变的集合
froSet = frozenset([1,2,4,5,6,4,3,6,4,323,3])
print(froSet)
#没有remove等方法
print(type(froSet))