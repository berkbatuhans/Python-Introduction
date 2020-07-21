# Veri Yapıları

# list, tuple, dict, set ve string

# Liste (list) Veri Yapısı

"""
    Listeler sıralı dizilimlerdir. Tuple ve string nesneleri ile aynı dilimleme (slicing) ve atlama (striding) işlemlerini destekler.
    Bir listenin elemanlarına çok kolay bir şekilde ulaşabilirsiniz. Üstelik listeler değiştirilebilir (mutable) elemanlara sahiptir.
    Yani bir listenin elemanlarını pozisyonlarını belirterek değiştirebilir veya silebilirsiniz. Sadece elemanları değil, eleman dilimlerini de silip değiştirebilir, ya da araya elklemeler
    yapabilirsiniz.

    Bir list nesnesi her tür veriyi (list ve tuple gibi veri yapılarını da) saklayabilir.

    Listeler [] köşeli parantezlerle gösterilir ve elemanları virgül ile birbirinden ayrılır.

"""

# Demet (Tuple) Veri Yapısı

"""
    En yalın haliyle Tuple, parantez içinde ve birbirlerinden virgül ile ayrılmış nesneler dizisidir.
    İndisleri sıfırdan başlar. Elemanları doğrudan değiştirilip silinemez (immutable). Dilimlenebilir. İçiçe kullanılabilir.
    
"""

T = (1, 2, 3, 4, 5)

T = T + T
print(T)
print(type(T))

print(T[2:5])

print(T[3:])

t1 = (1, 2, 3)
t2 = (4, 5)
t3 = (t1, t2)
print(t3)

lst = [1, 2, 3, 4]

t = (1, "ali", 62, 5.1, lst, 17, t3, 0, 0, t2)
print(t)

# t[0] = 5 #--> Hata! Çünkü tuple elemanlarına atama yapılamaz değiştirilemez.

print(t[4][1])  # Sorun yok çünkü değiştirilen elema bir listeye ait !!!

# Sözlük (dict) Veri Yapısı

"""
    Dict (sözlük) yapıları Anahtar: Değer çiftlerini süslü parantez {} içinde barındırırlar.
    Eleman çiftleri birbirinden virgül ile ayrılır. Anahtarlar özgün (unique) olmak zorundadır.
    Sözlük elemanları doğrudan değiştirilebilir. (Mutable). 
    Ekleme, silme, okuma gibi işlemler Anahtar: Değer çiftlerine birlikte uygulanır. 
"""

# Küme (set) Veri Yapısı

"""
    Küme, sözlüklerde olduğu gibi süslü parantezler içinde, virgülle ayrılan ve özgün
    elemanlardan oluşan sırasız bir kolleksiyondur. Endeksli değildir. Küme elemanlarına
    pozisyonlarına göre ulaşılamaz. Kümeler matematiksel set işlemlerini destekler.
"""

s = {1, 2, 3, 4, 5}

"""
    set(x) fonksiyonu x'in özgün elemanlarına göre ayrıştırır ve bir set haline dönüştürür.
    Böylece x'in iinde mükerrer elemanlar varsa, bu fonksiyon tarafından ayıklanmış olur.
"""

s1 = set("karışık bir liste")  # bir karakter katarının kümeye dönüştürülmesi
print(s1)
s2 = set({1, 2, 3, 4, 5, 1, 4})
print(s2)

"""
    Herhangi bir nesnenin kümeye dahil olup olmadığını **in** anahtar kelimesiyle kontrol ederiz.
"""

print(5 in s2)
# Return Value: True
print(7 in s2)
print(1 in s1)
print('k' in s1)
s1 = {1, 2, 3, 4, 6, 8, 10, 12}
s2 = {4, 5, 6, 7, 8, 9, 10}

print(s1, s2)

s3 = s1 - s2
print(s3)


s4 = s1 | s2
print(s4)

s5 = s1 & s2
print(s5)

s6 = s1 ^ s2
print(s6)

# Karakter Dizisi (str) Veri Yapısı

"""
    String yapıları ardışık Unicode karakterlerden oluşur. Ancak bu karakterlere doğrudan
    müdahale etmek, silmek veya ekleme yapmak mümkün değildir (immutable).
    u tür değişiklikleri, dilimleme ve ekleme gibi işlemler aracılığıyla gerçekleştirmek gerekir.
"""

