
from copy import deepcopy


def reversed_tom(liste: list[int]):
    """
    Return the reversed list.
    :param liste: list to be returned
    :return: returned list
    """
    liste.reverse()

    return liste


def permute(*args, **kwargs):
    """
    Allows you to exchange :
    - either two lists with the same index in the same matrix.
    - or two lists of different indexes of a matrix.
    - or the lists of same index of two different matrices.
    - or two lists of different indexes of two different matrices.
    :param args: Either one or two matrices.
    :type args: list[list[int]]
    :param kwargs: Either one or two indexes :
            - if one, it will be named "index.
            - if two, they will be named "index_1" and "index_2.
    :type kwargs: int
    :return: Either the processed matrix or the two processed matrices.
    :rtype: list[list[int]]
    """
    assert 1 <= len(args) <= 2
    assert 1 <= len(kwargs) <= 2
    if len(args) == 1:
        index_1 = kwargs.get("index_1", None)
        index_2 = kwargs.get("index_2", None)

        print(index_1)
        print(index_2)

        temp_matrix = deepcopy(args[0])

        args[0][index_1] = temp_matrix[index_2]
        args[0][index_2] = temp_matrix[index_1]

        return args[0]

    index = kwargs.get("index", None)
    index_1 = kwargs.get("index_1", None)
    index_2 = kwargs.get("index_2", None)

    if index:
        temp_matrix = deepcopy(args[0])

        args[0][index] = args[1][index]
        args[1][index] = temp_matrix[index]

        return args[0], args[1]

    temp_matrix = deepcopy(args[0])

    args[0][index_1] = args[1][index_2]
    args[1][index_2] = temp_matrix[index_1]

    return args[0], args[1]


def remontee(matrice: list[list[int]], colonne: list[int]) -> list:
    assert len(matrice) == len(colonne)

    if matrice[0][0] == 0:
        cpt = 1
        while matrice[cpt][0] == 0:
            cpt += 1
        matrice = permute(matrice, index = cpt)

    for i, elem in enumerate(colonne):
        matrice[i].append(elem)

    for j in range(len(matrice[0]) - 1):
        for i in range(1, len(matrice)):
            if matrice[i][j] != 0:
                piv = (matrice[i][j] / matrice[0][j]) * -1
                for e, elem in enumerate(matrice[i]):
                    if elem != 0:
                        matrice[i][e] /= piv

    # print(matrice)

    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            matrice[i][j] *= (1 / matrice[i][i])
            

    print(matrice)


if __name__ == '__main__':
    A = [
        [1, 3, 2],
        [0, -1, -1],
        [0, 0, 3]
    ]

    B = [64, -24, 31]

    print(remontee(A, B))

    # m1 = [
    #     [1, 2, 3],
    #     [13, 14, 15],
    #     [7, 8, 9]
    # ]
    #
    # m2 = [
    #     [10, 11, 12],
    #     [4, 5, 6],
    #     [16, 17, 18]
    # ]
    #
    # m1, m2 = permute(m1, m2, index = 1)
    #
    # print(m1)
    # print(m2)
