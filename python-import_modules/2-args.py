#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    # Récupère le nombre d'arguments passés au programme
    num_args = len(sys.argv) -1
    print("number of argument(s)", num_args, end = "")
    if num_args == 1:
        print("followed by argument:")
    elif num_args >= 1:
        print("followed by arguments:")
    else:
        print(".",)
# Imprime chaque argument avec sa position   
for i in range(1, len(sys.argv)):
    print(i, ":",sys.argv[i])