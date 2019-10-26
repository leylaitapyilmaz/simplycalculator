print("""
***************************
Hesap Makinesi

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi

****************************
""")

a=int(input("Bir sayı giriniz: "))
b=int(input("İkinci sayıyı giriniz: "))

işlem=int(input("Menüden bir işlem seçiniz:"))

if işlem == 1:
    print(" {} ile {} toplamı {}".format(a,b,(a+b)))
elif işlem==2:
    print(a-b)
elif işlem ==3 :
    print(a*b)
elif işlem == 4 :
    print(a/b)
else :
    print("Geçersiz İşlem Girdiniz!!!")
