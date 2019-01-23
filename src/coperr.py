import interpreter
from sys import argv

if len(argv) == 2:
    tree = interpreter.get_data(argv[1])

else:
    print("Cobalt.InputError : No input files specified")
    quit()

interpreter.eval_tree(tree)
