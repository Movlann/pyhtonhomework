import math 
a = int(input("Ucbucagin birinci terefini daxil edin: "))
b = int(input("Ucbucagin ikinci terefini daxil edin: "))
c = int(input("Ucbucagin ucuncu terefini daxil edin: "))
if a+b > c:
    if abs(a-b) < c:
        print("Ucbucaq berabersizliyi odenir")
    else:
        print("Ucbucaq berabersizliyi odenmir")
else:
    print("Ucbucaq berabersizliyi odenmir")