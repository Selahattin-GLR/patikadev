'''Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.'''

ilk_liste = [1, [[['a']], ['cat'], 2], [[[3]], 'dog'], 4, 5, [[[[[[12345]]], [[[[[[89765544, "33333333"]]]]]]]]]]


def liste_sadeleştirme(liste):
    yeni_liste = []

    for i in liste:

        if type(i) == list:
            yeni_liste += liste_sadeleştirme(i)

        else:
            yeni_liste.append(i)

    return yeni_liste


print(liste_sadeleştirme(ilk_liste))