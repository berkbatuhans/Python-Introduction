# TODO: Fibonacci sayılarını döndüren bir fonksiyon yazın. Parametre olarak verilen değer üst limit olsun.


def fibonacci(sinir):
    sayi1 = 0
    sayi2 = 1
    print(sayi1)
    print(sayi2)

    for i in range(sinir - 2):
        sayi3 = sayi1 + sayi2
        print(sayi3)
        sayi1 = sayi2
        sayi2 = sayi3


sinir = int(input("Lütfen sayı giriniz"))
fibonacci(sinir)