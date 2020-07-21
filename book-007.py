import math
# Akışın Denetlenmesi

# if
a = 1
b = 2
print("a = ", a, "b = ", b)
if a > b:
    print(a,"değeri", b,"'den büyüktür")
if a < b:
    print(a,"değeri", b,"'den küçüktür")
if b > 0:
    c = math.sqrt(4*a+b**2)
    print("(4*a+b**2)\'nin karekökü,", c,"\'dir ")


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