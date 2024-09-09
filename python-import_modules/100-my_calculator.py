#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":

    # Vérifier le nombre d'arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Récupérer les arguments
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator == '+':
        result = add(a, b)

    elif operator == '-':
        result = sub(a, b)

    elif operator == '*':
        result = mul(a, b)

    elif operator == '/':
        if b == 0:
            print("Error: Division by zero")
            sys.exit(1)
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Afficher le résultat
    print(f"{a} {operator} {b} = {result}")
