list1 = [32,5345,"23123"];
list2 = [3213,6547,8975,654,344];
print(list1>list2);
print(list1<list2); # 之比较列表的第一个元素

#列表拼接
print(list1 + list2);

#复制多次列表
print(list1 * 3);

list2 = list2 *2; #list2 *= 2
#判断某个元素是否在列表里面
print(123 in list1);
print(list2);

#如果要判断的数据存在于列表中的某一个元素，且这个元素也是一个列表
list3 = [123,456,[789,0,2]]

print(789 in list3);
print(789 in list3[2]);

#查找某一个元素在列表中出现了多少次
print(list2.count(3213));
#查找某个值的下标
print(list2.index(3213));
#反转某个列表，注意，源列表也会被反转
list2.reverse()
print(list2);
#排列列表，源列表会被排列
list2.sort() #注意，mix的列表无法排列
print(list2);
list4 = [3123,456354,74568,4324]
list4.sort(reverse = True)
print(list4);

print("列表是引用类型的，拷贝的区别")
ls1 = list4;
ls2 = list4[:]; #完全拷贝新的一个数组
print(ls1)
print(ls2)
print(list4)

list4.sort();
print(ls1)
print(ls2)
print(list4)

