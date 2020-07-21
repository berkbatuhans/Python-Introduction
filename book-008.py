# Fonksiyonlar def
"""
    Fonksiyon tanımında mutlaka gerekli olan elemanlar şunlardır.
    1. def anahtar kelimesi
    2. Geçerli bir fonksiyon adı
    3. Parantezler
    4. :
    5. fonksiyon gövdesi
"""


def ilk_fonksiyonum():
    pass


# pass
"""
    pass anahtar sözcüğü pasif bir joker işlevi görür.
    İçeriği netleşmemiş fonksiyonları tanımlarken pass komutu rahatlıkla kullanılabilir.
    
    Eğer bir fonksiyonun geri döndüreceği tanımlı bir değer yoksa, o fonksiyon None
    değeri döndürür. Bizim işlevsiz fonksiyonumuz da işte bu değeri  döndürür.
"""

print(ilk_fonksiyonum())

# Argümanlar

"""
    Parantez içindeki argümanların kullanılması bir zorunluluk değildir.
    Ama gerektiğinde istediğiniz sayı ve özelllikte argüman tanımlayabilirsiniz.
    
    Fonksiyon argümanlarını 4 gruba ayırabiliriz.
    
    1. Zorunlu argümanlar
    2. Anahtar kelimeli argümanlar
    3. Varsayılan argümanlar
    4. Değişken uzunluklu argümanlar
"""


## Zorunlu Argümanlar


def print_et(string):
    # string argümanını ekrana yazdırır
    print(string)


print_et("Günaydın!")

# Hata alır
# print_et("Günaydın", "hatalı ikinci parametre")


# Anahtar kelimeli argümanlar


"""
    Argümanın anahtar kelimeyle birlikte verilmesi, 
    özellikle çok argümanlı fonksiyonların kullanımında
    yazılımcıya daha esnek davranma imkanı sağlar.
    Argümanları tanımlandığı sırayla değil, istediğiniz sırada verebilirsiniz.
"""


def print_et(str1, str2):
    # string argümanlarını ekrana yazdırır
    print(str1, str2)


print_et(str2="Sana da Günaydın", str1="Merhaba!")
print_et(str1="Merhaba", str2="Sana da Günaydın")

# Varsayılan Argümanlar

"""
    Bazı durumlarda fonksiyon argümanlarından bazılarına öndeğer atanır.
    Böyle yapıldığında, o argüman fonksiyonun çağırılması sırasında argüman listesine eklenmezse,
    ön atama yapılmış varsayılan değerin geçerli olduğu kabul edilir.
    Bu yöntem de kullanıcı için önemli bir uygulama kolaylığı getirir.
"""


def kimNerede(ad, kent="İstanbul"):
    # Kişi adını ve hangi şehirde yaşadığını ekrana yazdırır.
    print("Adı: ", ad)
    print("Yaşadığı şehir: ", kent)
    print("-" * 30)  # 30 tane "-" yazdırır


print(kimNerede("Halil", "Keşan"))
print(kimNerede("Ahmet"))
print(kimNerede(kent="Bursa", ad="Cengiz"))


def degerBiteneKadarTire(deger="Berk Batuhan ŞAKAR"):
    print(deger)
    print("-" * (deger.__len__() + 10))


print(degerBiteneKadarTire("Berk Batuhan ŞAKAR1"))

# Değişken Uzunluklu Argümanlar

"""
    Bazı hallerde bir fonksiyona verilecek argümanların sayısı baştan net bir şekilde
    belirlenemez. Böyle durumlarda değişken argüman yapısı devreye girer.
    
    def fonksiyon(arg1, arg2, ..., *degiskken_arg):
        fonksiyon govdesi
    
    Yıldız (*) işaretiyle başlatılan değişken uzunluklu argüman bölümü boş bırakılabilir veya farklı
    sayıda argüman barındırabilir. 
"""


def kim(ad, kent, *ozellikler):
    # ad, kent ve kişisel özellikleri ekrana döker.
    print("Adı:", ad)
    print("Yaşadığı kent", kent)

    # kişisel özellikleri aynı string içinde topla

    ozel = ""
    for oz in ozellikler:
        ozel = ozel + " " + oz
        print("Özellikleri: ", ozel)
        print("-" * 50)


kim("Hale", "Antalya", "Esmer", "Siyah saçlı", "Ela Gözlü")

# Lambda Fonksiyonları

"""
    Standart def anahtar kelimesinin kullanılmadığı bazı küçük boyutlu fonksiyonlar
    anonim fonksiyonlar olarak adlandırılır. Bunları tanımlarken lambda anahtar sözcüğü kullanılır
    
    Lambda fonksiyonları yerel veya global değişkenlere ulaşamaz.
    Sadece kendi ve argüman listesindeki elemanları kullanır.
    
    Lambda fonksiyonlarını "tek satırlık fonksiyonlar" gibi düşünebiliriz.
    
    Bu fonksiyonların temel yapısı şu şekildedir.
    
    lambda [arg1, arg2, arg3, ...] : ifade
"""

topla = lambda arg1, arg2: arg1 + arg2

carp = lambda arg1, arg2, arg3: arg1 * arg2 * arg3

import math

hipotenus = lambda kenar1, kenar2: math.sqrt(kenar1 * kenar1 + kenar2 * kenar2)

print(topla(12, 27))
print(carp(11, 13, 17))
print(hipotenus(3, 4))


# return
"""
    Bir fonksiyon None değeri döndürdüğü gibi başka değer veya nesneler de döndürebilir.
    Fonksiyonun ne döndüreceği return anahtar kelimesiyle belirtilir.
    Bir değer veya nesne döndürmek, aynı zamanda o fonksiyon çağrısını sonlandırmak anlamına gelir.
"""


def toplamAl1(num1, num2):
    toplam = num1 + num2
    # işlem sonucunu bir değişkene aktar ve onu döndür
    return toplam


def toplamAl2(num1, num2):
    # doğrudan işlem sonucunu döndürür
    return num1 + num2
print("5 + 7 =", toplamAl1(5,7))
print("6 + 17 =", toplamAl2(6,17))

# Yerel ve Global Değişkenler

"""
    Bir fonksiyonun içinde tanımlanan bir değişken, yerel  bir etki alanına sahip olur.
    Yani sadece o fonksiyonun içinde ve alt fonksiyonlarda etkisini sürdürür.
    Fonksiyon etki alanının dışına çıktığında o değişken tanımsız hale gelir.
    
    Sınıflardaki katılım etkisi yerel değişkenler için de geçerlidir.
    Ana fonksiyonda tanımlanan bir değişken, alt fonksiyonlarda ( yavru fonksiyonlarda da) aynen
    tanınır. Ancak tersi doğru değildir. Yani alt (yavru) fonksiyonda tanımlanan bir yerel değişken ana (üst)
    kademeler için tanımsızdır.
"""

# Örnek Kod:

# s = "Fonksiyonun dışında tanımlı"
#
# def AnaFunction():
#     s1 = "s1 Fonksiyonun içinde tanımlı"
#     print("AnaFunction fonksiyonunun içi")
#     def YavruFunction():
#         s2 = "YavruFunction fonksiyonunun içi"
#         print("YavruFunction s = ", s)
#         print("YavruFunction s1 = ", s1)
#         print("YavruFunction s2 = ", s2)
#         print("-"*50)
#     YavruFunction()
#     print("AnaFunction s =", s)
#     print("AnaFunction s1 =", s1)
#     #print("AnaFunction s2 =", s2) #--> Bu satır hata verir



#AnaFunction()

#print("YavruFunction s=", s)
# print("YavruFunction s1=", s1) #--> Bu satır hata verir
# print("YavruFunction s2=", s2) #--> Bu satır hata verir


# global değişkeni kullanımı ile yukarıdaki örnekte alınan hatadan kurtulma.

s = "Fonksiyonun dışında tanımlı"

def AnaFunction1():
    global s1
    s1 = "s1 Fonksiyonun içinde tanımlı"
    print("AnaFunction1 fonksiyonunun içi")
    def YavruFunction():
        global s2
        s2 = "YavruFunction fonksiyonunun içi"
        print("YavruFunction s = ", s)
        print("YavruFunction s1 = ", s1)
        print("YavruFunction s2 = ", s2)
        print("-"*50)
    YavruFunction()
    print("AnaFunction s =", s)
    print("AnaFunction s1 =", s1)
    #print("AnaFunction s2 =", s2) #--> Bu satır hata verir



AnaFunction1()

print("YavruFunction s=", s)
print("YavruFunction s1=", s1) #--> Bu satır hata verir
print("YavruFunction s2=", s2) #--> Bu satır hata verir





