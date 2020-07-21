import math

# Akışın Denetlenmesi

# if
a = 1
b = 2
print("a = ", a, "b = ", b)
if a > b:
    print(a, "değeri", b, "'den büyüktür")
if a < b:
    print(a, "değeri", b, "'den küçüktür")
if b > 0:
    c = math.sqrt(4 * a + b ** 2)
    print("(4*a+b**2)\'nin karekökü,", c, "\'dir ")

# if - else

x = 1
y = 1

if x == y:
    print("Eşittir")
else:
    print("Eşit Değildir")

# if - elif - else

# Eğer tek bir koşul değil'de, daha fazla koşul peş peşe değerlendirmeye alınırsa bu kez de
# if - elif - else ifadeleri kullanılır.

adlar = ["Berk", "Burak", "Ahmet", "John", "Veli"]
for ad in adlar:
    if ad == 'Berk':
        print("Benim Adım: ", ad)
    elif ad == 'Burak':
        print("Arkadaşımın Adı: ", ad)
    elif ad == 'John':
        print("Arkadaşın", ad, "bir İngilizdir.")
    else:
        print(ad, "adında birini tanımıyorum.")

# Döngüler

# For Döngüsü
liste1 = [99, 98, 97]
liste2 = [1, 3, 7, 11, "çiçek", "böcek", liste1]

for n in liste2:
    print(n)

# While Döngüsü
print("WHILE DÖNGÜSÜ")
i = 0
while i < 5:
    print(i)
    i += 1

i = 0

# break ile döngünün kırılması
print("BREAK KOMUTU")
while True:
    print(i)
    i += 1
    if i >= 5:
        break

# return komutu ile döngü kırılması
# Döngüyü kırmakla kalmaz, içinde bulunduğu fonksiyonu da sonlandırır.

# continue komutu
# Çalıştığında kendinden sonraki işlemleri atlayıp, döngünün başına dönmeyi sağlar.
print("CONTINUE KOMUTU")
# TEK SAYILARI EKRANA BASAN ÖRNEK
i = 0
while True:
    i += 1
    if i % 2 == 0:
        continue
    elif i > 10:
        break
    else:
        print(i)


# pass komutu
# Hiç bir eylemsel işlevi yoktur. Bu komutu henüz kodlarını yazmadığımız fonksiyonları
# tanımlarken veya herhangi bir işlem yapılmamasının istediğimiz koşullarda kullanmamız mümkün


def yeni_fonksiyon():
    pass


yeni_fonksiyon()

# range Fonksiyonu

# range(son)
# range(ilk, son)
# range(ilk, son, adım)

l1 = []
l2 = []
l3 = []
for i in range(17):
    l1.append(i)
print(l1)
for i in range(2, 11):
    l2.append(i)
print(l2)
for i in range(5, 24, 3):
    l3.append(i)
print(l3)


