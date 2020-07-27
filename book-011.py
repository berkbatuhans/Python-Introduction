# Karakter Dizisi (str) Veri yapıları

# Temel Özellikleri

# - Çift (") veya Tek (') tırnaklar arasına yazılır.
# - Karakter dizilimleridir.
# - Dizi (array) şeklinde davranırlar.
# - Elemanları değiştirilemez (immutable)
# - Dilimlenebilir (sliceable)


# String Nesnelerinde Dilimleme ve Birleştirme Yapmak


# s[ilk:son:adım]
"""
     İlk, son ve adım hem pozitif (+), hem de negatif (-) değer alabilir.
     Adımın varsayılan değeri 1'dir. 2 olursa birer atlayarak, 3 olursa ikişer atlayarak anlamına gelir.
     Negatif adım sondan başa doğru çalışır.
     Negatif başlangıç ve son değerleri stringin sonundan başa doğru sayılır.
     Örneğin -1 stringin en son elemanını tarif eder
"""

name = "Berk Batuhan ŞAKAR"

# Başlangıçtan İtibaren ilk 4 karakteri al
print(name[:4])

# Başlangıçtan itibaren ilk 4 karakteri al
print(name[0:4])

# 3. karakterden başla, 8 nolu karaktere kadar hepsini al
print(name[3:9])

# 4.karakterden sonuna kadar tümünü al
print(name[3:])

# Son iki karakter hariç hepsini al
print(name[:-2])

# Son 10 karakterin baştan sekizini al (Bir üst satırla aynı)
print(name[-10:-2])

# İlk 3 karakterden sonra araya "abc" ekle
print(name[:3] + "abc" + name[3:])

# Baştan 2, sondan 4 karakteri alıp birleştir (arayı iptal et)
print(name[:2]+name[-4:])

# Karakterlerin yerleşimini kolay hesaplamak için rakamla dolduralım
s = "01234567890123456789"
print("s =", s)
print(f"s stringinin uzunluğu (len(s)) =", len(s))
print("Baştan ilk 4 karakter: s[:4] = ", s[:4])
print("Baştan ilk 4 karakter: s[0:4] = ", s[0:4])



