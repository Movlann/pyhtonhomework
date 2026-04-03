u = "Movlan"
p = "2008"
i = 0
while i < 3:
    username = input("Istifadeci adinizi daxil edin: ")
    password = input("Parolunuzu daxil edin: ")
    if username == u and password == p:
        print("Sisteme giris edildi")
        break
    else:
        i+= 1
        print("Istifadeci adi ve ya parol yanlisdir")
        print("Qalan cehdiniz: ", 3-i )
    if i == 3:
        print("Hesabiniz bloklandi")

