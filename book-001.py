import config

name = "Berk Batuhan"
surname = "ŞAKAR"
print(f"Hello, {name} {surname}")

POSTGRES_URL = config.CONFIG['postgresUrl']
POSTGRES_USER: str = config.CONFIG['postgresUser']
POSTGRES_PASS: int = config.CONFIG['postgresPass']
POSTGRES_DB = config.CONFIG['postgresDb']
# DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'\
#     .format(user=POSTGRES_USER,
#             pw=POSTGRES_PASS,
#             url=POSTGRES_URL,
#             db=POSTGRES_DB)
# config['SQLALCHEMY_DATABASE_URI'] = DB_URL

# dir() komutu parametresiz olarak verildiğinde
# Python'un o aşamada tanıdığı üst düzey
# fonksiyon, sabit veya değişkenlerin listesi alınır

# Komut:
# print(dir())
# Çıktı:
# ['POSTGRES_DB', 'POSTGRES_PASS', 'POSTGRES_URL', 'POSTGRES_USER', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'config', 'name', 'surname']
# print(help())

# Sabitler

AD = "Berk Batuhan"
SOYAD = "ŞAKAR"

print(f"{AD}-{SOYAD}")
#Değişkenler
x = 20
y = 6
z = 21.4
q = "6"

# Toplama
toplama = x + y
print(f"Toplama: {toplama}")

# Çıkarma
cikarma = x - y
print(f"Çıkarma: {cikarma}")

# Çarpma
carpma = x * y
print(f"Çarpma: {carpma}")

# Bölme
bolme = x / y
print(f"Bölme: {bolme}")

# Bölümden elde edilen tam kısmın bulunması
bolumtamkismi = x // y
print(f"Bölümün Tam Kısmı: {bolumtamkismi}")

# Bölümden elde edilen kalan kısmın bulunması
bolumkalankismi = x % y
print(f"Bölümün Kalan Kısmı: {bolumkalankismi}")

# x sayisinin y üssünün alinmasi
usalma = x ** y
print(f"x sayisinin y Üssü: {usalma}")

# x sayisinin negatif degeri
negatifdeger = -x
print(f"Negatif Değer {negatifdeger}")

# x sayisinin mutlak değeri
mutlakdeger = abs(x)
print(f"Mutlak Değer: {mutlakdeger}")

'''
    x in y ile bölünmesinden elde edilen tam ve kalan kısımların iki tam sayıdan oluşan tuple
    halinde döndürülmesi
'''
tamvekalan = divmod(x, y)
print(f"Tam ve Kalan: {tamvekalan}")

# x in y üssünün alınması ( x**y ile aynı sonucu verir)
powUsAlma = pow(x, y)
print(f"Pow ile x sayisinin y Üssü: {powUsAlma}")

# pow(x,y)%z değeri
powUsAlmaModu = pow(x, y, 4)
print(f"Pow ile x sayisinin y Üssü: {powUsAlmaModu}")

# x'in n haneye yuvarlanması
yuvarlama = round(z, 3)
print(f"Yuvarlama: {yuvarlama}")

# on tabanlı i sayısının iki tabanına (binary) dönüştürülmüş olarak
# gösterimi (string)

binary = bin(x)
print(f"Binary: {binary}")

# on tabanlı i sayısının onaltılık tabanına (hexedecimal) dönüştürülmüş olarak
# gösterimi (string)

hexedecimal = hex(x)
print(f"Hexedecimal: {hexedecimal}")

# Sayının tam sayıya dönüştürülmesi (Yuvarlama yapılmaz)
tamsayidonustur = int(z)
print(f"Tamsayı Dönüştürme: {tamsayidonustur}")

# TODO: Sayının tam sayıya dönüştürülmesi (Yuvarlama yapılmaz)
# tamsayi = int(q,6)
# print(f"Tamsayı: {tamsayi}")

# On tabanlı i sayısının sekizlik tabanına (octal) dönüştürülmüş olarak gösterimi (string)
octal = oct(x)
print(f"Octal: {octal}")

# On tabanlı sayının string hale dönüştürülmüş halini üretir.
StringCevir = str(x)
print(f"String: {type(StringCevir)} {StringCevir}")

# Boolean İfadeler

IsActive: bool = True
IsActive: bool = 1
IsActive: bool = 0
Gender = False
Gender = True
print(bool(IsActive))

# TODO: Kayan noktalı sayılar
# TODO: Decimal sayılar
# TODO: Kompleks sayılar

# Karakter Dizileri (Strings)

s1 = "Berk "
s2 = "Batuhan ŞAKAR"
s3 = s1 + s2
print(s3)

s3 *= 3
print(s3)
# Çıktı Berk Batuhan ŞAKARBerk Batuhan ŞAKARBerk Batuhan ŞAKAR

# Listeler (Lists)

## Boş Liste
liste1 = []

##
liste2 = [1, 2, 3, 4]
print(liste2)

## Liste elemanları değiştirilebilir (mutable)
liste2[1] = 11
print(liste2)

## Farklı Tiplerdeki nesneler aynı listenin içinde yer alabilirler:

liste = [1, "string", liste1, ('abc', 'xxx', 5)]
print(liste)

# Demetler (Tuples)

tuple = (123, 'a', ['X', 'y', 5], (1, 2, 3), 5, 'xyz')

print(tuple)

# Elemanları doğrudan değiştirilemez aşağdaki şekilde yazılan kod hata verir.
# tuple[0] = 1

# tuple2 = tuple + tuple[0]
# print(tuple2)

# Kümeler (Sets)

kume = set()
print(kume)

# Kalabalık kümelerde aradığımız elemanın var olup olmadığını kolayca kontrol edebiliriz.
kume1 = {0, 1, 2, 3, 4, 5}
test = 2 in kume1
test2 = 11 in kume1

print(test)
print(test2)

# Sözlükler ( Dicts )

notlar = {'ali': 90, 'neriman': 93, 'emre': 10}
notlar['emre'] = 99 # anahtarı emre olan elemanın değeri değiştiriliyor.
print(notlar['emre'])
del notlar['neriman'] # neriman olan eleman siliniyor.
print(notlar)

# Operatörler

# Operatör  | İşlev
# +         | Toplama
# -         | Çıkarma
# *         | Çarpma
# /         | Bölme
# //        | Tam sayı bölme
# **        | Üs alma
# %         | Kalanı hesaplama

# İkili İşlem Operatörleri

# Operatör  | İşlev
# <<        | Sola 1 bit kaydırma
# >>        | Sağa 1 bit kaydırma
# &         | AND
# |         | OR
# ^         | XOR
# ~         | NOT

# Kıyaslama Operatörleri
# Operatör  | İşlev
# <         | Küçüktür
# >         | Büyüktür
# <=        | Küçük veya eşit
# >=        | Büyük veya eşit
# ==        | Eşit
# !=        | Eşit değil
# is        | Değer ve ID eşitliği
# in        | Mevcut

# Atama Operatörleri
# Operatör  | İşlev
# +=        | Artırarak ata
# -=        | Eksilterek ata
# *=        | Çarparak ata
# /=        | Bölerek ata
# **=       | Üs alarak ata
# //=       | Tamsayı bölerek ata
# %=        | Kalanı hesaplayarak ata
# <<=       | Sola kaydırarak ata
# >>=       | Sağa kaydırarak ata
# &=        | AND uygulayarak ata
# |=        | OR uygulayarak ata
# ^=        | XOR uygulayarak ata

# Operatörlerin öncelik sıralaması

# Öncelik   |   Operatör            |   İşlev
# 1         |   OR                  |   Mantıksal OR
# 2         |   AND                 |   Mantıksal AND
# 3         |   NOT                 |   Mantıksal NOT
# 4         | <,<=,>,>=,==,!=,is,in |   Kıyaslamalar
# 5         | |                     |   İkilik OR
# 6         | ^                     |   İkilik XOR
# 7         | &                     |   İkilik AND
# 8         | <<,>>                 |   İkilik sola ve sağa kaydırma
# 9         | +, -                  |   Toplama, çıkarma
# 10        | *,/,//,%              |   Çarpma, bölme, kalan
# 11        | +x, -x, ~x            |   Birli (unary) işlemler
# 12        | **                    |   Üs alma
# 13        | ()                    |   Parantez