'''Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.'''

ilk_liste = [0, 1, 2, [[3, 4, 5]], [4, 5, 6], [[[5, 7, 8, 9, [1, 2, 3], "wert", 111]]], [[[[[[["abcd"]]]]]]]]

def liste_ters(liste):
    liste.reverse()

    for i in liste:

        if type(i) == list:
            liste_ters(i)

    return liste


print(liste_ters(ilk_liste))