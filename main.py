
from copy import deepcopy


def reversedTom(liste: list[int]):
    liste.reverse()
    return liste


def remontee(Matrice: list[list[int]], Colonne: list[int]) -> list[float]:
    z = Colonne[-1] / Matrice[-1][-1]
    y = Colonne[-2] * -1 - z
    x = Colonne[-3] - Matrice[-3][-2] * y - Matrice[-3][-1] * z

    # test = [
    #     Colonne[]
    # ]
    Matrice.reverse()
    print([(Colonne[-(i+1)] / reversedTom(elem)[:i+1][0]) for i, elem in enumerate(Matrice)])
    a = [x, y, z]
    a.reverse()
    return a


def permute(matrice1: list[list[int]], matrice2: list[list[int]], indexLigne1: int,  indexLigne2: int)\
        -> tuple[list[list[int]], list[list[int]]]:
    """
    Permute deux lignes d'index choisi de deux matrices.
    :param matrice1: Matrice à laquelle on permute la ligne d'indice indexLigne1
                avec la ligne d'indice indexLigne2 de la matrice2.
    :param matrice2: Matrice à laquelle on permute la ligne d'indice indexLigne2
                    avec la ligne d'indice indexLigne1 de la matrice1.
    :param indexLigne1: Index de la ligne de la matrice1 à permmuter.
    :param indexLigne2: Index de la ligne de la matrice2 à permmuter.
    :return: Les deux matrices permutées.
    """
    nouvelleMatrice1 = deepcopy(matrice1)
    nouvelleMatrice2 = deepcopy(matrice2)

    nouvelleMatrice1[indexLigne1] = matrice2[indexLigne2]
    nouvelleMatrice2[indexLigne2] = matrice1[indexLigne1]

    return nouvelleMatrice1, nouvelleMatrice2


if __name__ == '__main__':
    # A = [
    #     [1, 3, 2],
    #     [0, -1, -1],
    #     [0, 0, 3]
    # ]
    #
    # B = [64, -24, 31]
    #
    # print(remontee(A, B))

    m1 = [
        [1, 2, 3],
        [13, 14, 15],
        [7, 8, 9]
    ]

    m2 = [
        [10, 11, 12],
        [4, 5, 6],
        [16, 17, 18]
    ]

    m1, m2 = permute(m1, m2, 1, 1)

    print(m1)
    print(m2)

