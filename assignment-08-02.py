# TODO: Collatz dizisi üreten fonksiyonu yazın.

def collatz(n):
    enbuyuk = n
    uzunluk = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        print(n)
        uzunluk += 1
        if n > enbuyuk:
            enbuyuk = n
    return uzunluk, enbuyuk


print(collatz(13))
