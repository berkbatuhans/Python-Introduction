#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# Page 150 - Miras (Inheritance)


class Kimlik:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def __str__(self):
        return "Ad: {ad} - Yaş: {yas}".format(ad=self.ad, yas=self.yas)


class Ogrenci(Kimlik):
    def __init__(self, ad, yas, notu):
        Kimlik.__init__(self, ad, yas)
        self.notu = notu

    def __str__(self):
        return "{kimlik} - Notu: {notu}".format(kimlik=Kimlik.__str__(self), notu=self.notu)


def test():
    o1 = Ogrenci("Berk", 25, 86)
    print(o1)


if __name__ == "__main__":
    test()

