#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# Çoklu Miras ( Multiple Inheritance)


class Kimlik:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def __str__(self):
        return "Ad: {ad} - Yaş: {yas}".format(ad=self.ad, yas=self.yas)


class Erisim():
    def __init__(self, tel, eposta):
        self.tel = tel
        self.eposta = eposta

    def epostaDegis(self, eposta):
        self.eposta = eposta

    def __str__(self):
        return self.tel + " - " + self.eposta


class Ogrenci(Kimlik, Erisim): #Kimlik ve Erişim sınıflarından miras
    def __init__(self, ad, yas, notu, tel, eposta):
        Kimlik.__init__(self, ad, yas) # Kimlik sınıfının örneği (instance oluşturuluyor)
        Erisim.__init__(self, tel, eposta) #Erişim sınıfı örneği oluşturuluyor.
        self.notu = notu

    def epostaDegis(self, eposta): #Overriding (geçersizleştirme) uygulanıyor.
        self.eposta = "Epostalar iptal edildi"

    def __str__(self):
        return "{kimlik} - Erişim: {erisim} - Notu: {notu}".format(kimlik=Kimlik.__str__(self), erisim=Erisim.__str__(self), notu=self.notu)


def test():
    o1 = Ogrenci("Berk", 25, 86, "0555 555 55 55", "berk@berk.com")
    print(o1)
    o1.epostaDegis("berk@y.com")
    print(o1)


if __name__ == "__main__":
    test()