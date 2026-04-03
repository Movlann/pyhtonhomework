list1 = [1, 2, 3, 4, 5]
list2 = list1
list1[1] = 0
print(list2)
#list uzerinde deyisiklik edildikde ona beraber olan listde deyisir
list3 = [1, 2, 3, 4, 5]
list4 = list3.copy()
list3[1] = 0
print(list4)