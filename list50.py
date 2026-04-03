list1 = [1, 2, 3, 4, 5]
list2 = [6, 7]
list3 = list1 + list2
print(list3)
#listleri birlesdirmek ucun yeni list yaratmaq lazimdir
list3 = [1, 2, 3, 4, 5]
list4 = [6, 7]
list3.extend(list4)
print(list3)