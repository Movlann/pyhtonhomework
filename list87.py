#list deyisdirile biler. Ona gore cox metod var (append(), remove(), insert() ve s.)
list1 = [1, 2, 3, 4, 5]
list1.append(6)
print(list1)
#tuple deyisdirile bilmir. Ona gore az metod var. (index(), count()) Tuple uzerinde deyisiklikler etmek ucun evvelce onu liste cevirmek lazimdir
tuple1 = (1, 2, 3, 4, 5)
list2 = list(tuple1)
list2.append(6)
tuple1 = tuple(list2)
print(tuple1)