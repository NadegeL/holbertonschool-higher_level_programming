#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Remplir les tuples avec des zéros pour les valeurs manquantes
    tuple_a_padded = tuple_a + (0, ) * (2 - len(tuple_a))
    tuple_b_padded = tuple_b + (0, ) * (2 - len(tuple_b))

# Utiliser uniquement les deux premiers éléments
    final_tuple = (tuple_a_padded[0] + tuple_b_padded[0],
                   tuple_a_padded[1] + tuple_b_padded[1])

    return final_tuple
